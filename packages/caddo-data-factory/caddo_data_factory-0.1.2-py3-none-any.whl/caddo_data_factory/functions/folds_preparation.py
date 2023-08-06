from caddo_data_factory.functions.folding_enum import FoldingEnum
from caddo_data_factory.functions.folding_methods import FoldingMethods
from caddo_file_parser.models.run import Run
from caddo_file_parser.models.index_set import IndexSet
from caddo_file_parser.settings.generation_settings import GenerationSettings

def get_folding_method(settings: GenerationSettings):
    folding_method = settings.data_splitting_folding_method
    match FoldingEnum[folding_method]:
        case FoldingEnum.KFOLD:
            return FoldingMethods.kfold_method
        case FoldingEnum.SKFOLD:
            return FoldingMethods.skfold_method


class FoldsPreparation:
    def __init__(self, settings_path=''):
        self.settings_path = settings_path

    def get_folds_dataset(self, dataset, settings: GenerationSettings):
        runs = []
        folding_method = get_folding_method(settings)
        for run in range(settings.data_splitting_runs):
            index_sets = []
            i = 0
            fold = folding_method(self, settings.data_splitting_folding_number,
                                  settings.data_splitting_folding_seeds_from_list, run)
            for train_index, val_index in fold.split(dataset):
                index_set: IndexSet = IndexSet(number=i,
                                               train_indexes=train_index.tolist(),
                                               test_indexes=val_index.tolist(),
                                               seed=settings.data_splitting_folding_seeds_from_list[run])
                i += 1
                index_sets.append(index_set)
            single_run = Run(number=run, index_sets=index_sets, seed=settings.data_splitting_folding_seeds_from_list[run])
            runs.append(single_run)
        return runs
