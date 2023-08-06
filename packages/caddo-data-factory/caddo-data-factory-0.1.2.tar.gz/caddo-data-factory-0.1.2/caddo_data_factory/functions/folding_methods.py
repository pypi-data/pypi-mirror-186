from sklearn.model_selection import StratifiedKFold, KFold


class FoldingMethods:

    def __init__(self, settings_path=''):
        self.settings_path = settings_path

    def kfold_method(self, n_splits, seeds, run):
        return KFold(n_splits=n_splits, shuffle=True, random_state=seeds[run])

    def skfold_method(self, n_splits, seeds, run):
        return StratifiedKFold(n_splits=n_splits, shuffle=True, random_state=seeds[run])
