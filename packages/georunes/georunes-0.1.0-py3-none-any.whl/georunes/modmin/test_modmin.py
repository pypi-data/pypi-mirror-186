from georunes.tools.filemanager import FileManager
from georunes.modmin.norm.cipw import CIPWNorm
from georunes.modmin.optim.bvls import BVLS
from georunes.modmin.optim.gd import GradientDescent
from georunes.modmin.optim.randsearch import RandomSearch
from georunes.modmin.optim.nnls import NNLS

filemanager = FileManager.get_instance()

#source = "D:/Dev/py/graph/geoglyph/georunes/modmin/cipw.csv"
source2 = "D:/Dev/py/graph/geoglyph/georunes/modmin/cipw2.csv"

#data = filemanager.read_file(source)

data2 = filemanager.read_file(source2)
minerals = filemanager.read_file("D:/Dev/py/graph/geoglyph/georunes/modmin/minerals_t.csv")

vb = 2

cipw = CIPWNorm(verbose=vb)
nnls = NNLS(verbose=vb)
bvls = BVLS(verbose=vb)
rs = RandomSearch(verbose=vb, dist_func="max")
gd = GradientDescent(verbose=3, dist_func="SMAPE")

# cipw.compute(data, skip_cols=1, minor_included=True,  co2_calcite=1, co2_cancrinite=0)


max_minerals = {}
min_minerals = {}
# max_minerals["Hematite"] = 0.12
min_minerals["Hematite"] = 0.04  # check if it is a full mineral, not element of solid solution
ratios = {"PG": [["Albite", "Anorthite"], [60, 40]],
          "Mica": [["Biotite", "Muscovite"], [8, 12]]}
ratios = {"PG": [["Albite", "Anorthite"], [50, 50]],
          "Mica": [["Biotite", "Muscovite"], [10, 10]]}

ratios=None
bvls.compute(data2, skip_cols=4, raw_minerals_data= minerals, ignore_oxides=("LOI",), ratios = ratios,
max_minerals = max_minerals, min_minerals=min_minerals, unfillable_partitions_allowed = False)
#
# nnls.compute(data2, skip_cols=4, raw_minerals_data= minerals, ignore_oxides=("LOI",), ratios= ratios)


starter = {
    "Quartz": 19,
    "Hematite": 10,
    "Orthoclase": 15,
    'PG': 38,
    'Mica': 18
}

# p,s = gd.compute(data2, skip_cols=5, raw_minerals_data= minerals, ignore_oxides=("LOI",),
#                  max_iter=100000, learn_rate=0.0001, ratios=ratios, max_minerals = max_minerals, min_minerals=min_minerals,
#                  starting_partition = starter
#                  )


# p,s = rs.compute(data2, skip_cols=4, raw_minerals_data= minerals, ignore_oxides=("LOI"), #starting_partition = starter,
#                  max_iter=1000, search_semiedge=0.0001, ratios=ratios, max_minerals = max_minerals, min_minerals=min_minerals,
#                  unfillable_partitions_allowed = False
#                  )





