import pandas as pd
from tqdm.auto import tqdm
tqdm.pandas()

from scattertext.termranking.AbsoluteFrequencyRanker import AbsoluteFrequencyRanker


class PMICompactor(object):
    def __init__(
            self,
            term_ranker=AbsoluteFrequencyRanker,
            minimum_term_count: int = 2,
            number_terms_per_length: int = 2000,
            show_progress=True
    ):
        '''

        Parameters
        ----------
        term_ranker : TermRanker
            Default AbsoluteFrequencyRanker
        minimum_term_count : int
            Default 2
        number_terms_per_length : int
            Select X top PMI terms per ngram length
            Default 2000
        show_progress: bool
            Shows TQDM for PMI filtering
        '''
        self.term_ranker = term_ranker
        self.minimum_term_count = minimum_term_count
        self.number_terms_per_length = number_terms_per_length
        self.show_progress = show_progress

    def compact(self, term_doc_matrix, non_text=False):
        '''
        Parameters
        ----------
        term_doc_matrix : TermDocMatrix
            Term document matrix object to compact
        non_text : bool
            Use non-text features instead of terms

        Returns
        -------
        New term doc matrix
        '''
        freqs = self.__get_term_frequencies(non_text, term_doc_matrix)
        pmi_df = self.__get_pmi_df(freqs)[lambda df: df.Count >= self.minimum_term_count]

        threshold_df = self.__get_ngram_length_pmi_thresholds(pmi_df)

        filtered_pmi_df = pd.merge(
            pmi_df,
            threshold_df,
            left_on='Len',
            right_index=True
        )[lambda df: df.PMI < df.PMIThreshold]

        terms_to_remove = list(filtered_pmi_df.Term)

        return term_doc_matrix.remove_terms(
            terms_to_remove, non_text
        ).remove_infrequent_words(
            self.minimum_term_count, term_ranker=self.term_ranker, non_text=non_text
        )

    def __get_term_frequencies(self, non_text, term_doc_matrix):
        ranker = self.term_ranker(term_doc_matrix)
        if non_text:
            ranker = ranker.use_non_text_features()
        freqs = ranker.get_ranks().sum(axis=1)
        return freqs

    def __get_ngram_length_pmi_thresholds(self, pmi_df):
        return pmi_df[lambda df: (df.Len > 1) & (df.Count >= self.minimum_term_count)].groupby(
            'Len'
        ).apply(
            lambda gdf: pd.series({'PMI': 0}) if len(gdf) <= self.number_terms_per_length else gdf.sort_values(
                by='PMI', ascending=False
            ).iloc[self.number_terms_per_length][['PMI']]
        ).rename(columns={'PMI': 'PMIThreshold'})

    def __get_pmi_df(self, freqs):
        #ngram_lens = np.array([len(x.split()) for x in freqs.index])
        wc = dict(pd.DataFrame({
            'Len': [len(x.split()) for x in freqs.index],
            'Freq': freqs
        }).groupby('Len').sum()['Freq'])

        def prob(ngram):

            if len(ngram) == 0:
                return 1
            joined_ngram = ' '.join(ngram)
            if joined_ngram in freqs:
                return freqs.loc[joined_ngram] / (wc[len(ngram)] - len(ngram) + 1)
            return freqs.loc[ngram[0]] / wc[1] * prob(ngram[1:])

        apply = lambda df: df.apply
        if self.show_progress:
            apply = lambda df: df.progress_apply

        return pd.DataFrame({'Count': freqs}).reset_index(
        ).rename(
            columns={'term': 'Term'}
        ).assign(
            Len=lambda df: df.Term.apply(lambda x: len(x.split())),
        )[lambda df: df.Len > 1].assign(
            PMI = lambda df: apply(df.Term)(lambda x: prob(x.split()))
#            PMI=lambda df: apply(df)(
#                lambda r: None if r.Len < 2 else np.log(
#                    (r.Count / wc) / (np.prod(list(freqs[x] / wc for x in r.Term.split())))
#                ),
#                axis=1
#            )
        )
