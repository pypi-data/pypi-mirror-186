from pollination_dsl.dag import Inputs, DAG, task, Outputs
from dataclasses import dataclass
from pollination.honeybee_radiance.raytrace import RayTracingDaylightFactor

# input/output alias
from pollination.alias.inputs.model import hbjson_model_grid_input
from pollination.alias.inputs.radiancepar import rad_par_daylight_factor_input
from pollination.alias.inputs.grid import grid_filter_input, \
    min_sensor_count_input, cpu_count
from pollination.alias.outputs.daylight import daylight_factor_results


from ._prepare_folder import DaylightFactorPrepareFolder
from ._postprocess_results import DaylightFactorPostProcessResults


@dataclass
class DaylightFactorEntryPoint(DAG):
    """Daylight factor entry point."""

    # inputs
    model = Inputs.file(
        description='A Honeybee Model in either JSON or Pkl format. This can also '
        'be a zipped honeybee-radiance folder.',
        extensions=['json', 'hbjson', 'pkl', 'hbpkl', 'zip'],
        alias=hbjson_model_grid_input
    )

    cpu_count = Inputs.int(
        default=50,
        description='The maximum number of CPUs for parallel execution. This will be '
        'used to determine the number of sensors run by each worker.',
        spec={'type': 'integer', 'minimum': 1},
        alias=cpu_count
    )

    min_sensor_count = Inputs.int(
        description='The minimum number of sensors in each sensor grid after '
        'redistributing the sensors based on cpu_count. This value takes '
        'precedence over the cpu_count and can be used to ensure that '
        'the parallelization does not result in generating unnecessarily small '
        'sensor grids. The default value is set to 1, which means that the '
        'cpu_count is always respected.', default=500,
        spec={'type': 'integer', 'minimum': 1},
        alias=min_sensor_count_input
    )

    radiance_parameters = Inputs.str(
        description='The radiance parameters for ray tracing',
        default='-ab 2 -aa 0.1 -ad 2048 -ar 64',
        alias=rad_par_daylight_factor_input
    )

    grid_filter = Inputs.str(
        description='Text for a grid identifier or a pattern to filter the sensor grids '
        'of the model that are simulated. For instance, first_floor_* will simulate '
        'only the sensor grids that have an identifier that starts with '
        'first_floor_. By default, all grids in the model will be simulated.',
        default='*',
        alias=grid_filter_input
    )

    @task(template=DaylightFactorPrepareFolder)
    def prepare_daylight_factor_folder(
            self, cpu_count=cpu_count, min_sensor_count=min_sensor_count,
            grid_filter=grid_filter, model=model
    ):
        return [
            {
                'from': DaylightFactorPrepareFolder()._outputs.model_folder,
                'to': 'model'
            },
            {
                'from': DaylightFactorPrepareFolder()._outputs.resources,
                'to': 'resources'
            },
            {
                'from': DaylightFactorPrepareFolder()._outputs.initial_results,
                'to': 'initial_results'
            },
            {
                'from': DaylightFactorPrepareFolder()._outputs.sensor_grids
            }
        ]

    @task(
        template=RayTracingDaylightFactor,
        needs=[prepare_daylight_factor_folder],
        loop=prepare_daylight_factor_folder._outputs.sensor_grids,
        sub_folder='initial_results/{{item.full_id}}',  # subfolder for each grid
        sub_paths={
            'grid': 'grid/{{item.full_id}}.pts',
            'scene_file': 'scene.oct',
            'bsdf': 'bsdf'
        }
    )
    def daylight_factor_ray_tracing(
        self,
        radiance_parameters=radiance_parameters,
        scene_file=prepare_daylight_factor_folder._outputs.resources,
        grid=prepare_daylight_factor_folder._outputs.resources,
        bsdf_folder=prepare_daylight_factor_folder._outputs.model_folder
    ):
        return [
            {
                'from': RayTracingDaylightFactor()._outputs.result,
                'to': '../{{item.name}}.res'
            }
        ]

    @task(
        template=DaylightFactorPostProcessResults,
        needs=[daylight_factor_ray_tracing]
    )
    def post_process_results(
            self, results_folder='initial_results',
            grids_info='resources/grids_info.json'
    ):
        return [
            {
                'from': DaylightFactorPostProcessResults()._outputs.results,
                'to': 'results'
            }
        ]

    results = Outputs.folder(
        source='results', description='Folder with raw result files '
        '(.res) that contain daylight factor values for each sensor.',
        alias=daylight_factor_results
    )
