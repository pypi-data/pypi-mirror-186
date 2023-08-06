
import "https://gitlab.com/intelliseq/workflows/raw/bco-merge@1.4.0/src/main/wdl/tasks/bco-merge/latest/bco-merge.wdl" as bco_merge_task


workflow pipeline_name_TAG {


  String pipeline_name = "pipeline_name_TAG"
  String pipeline_version = "latest"


  #1 first task to call



  # after all regular tasks merge bco
  # Merge bco, stdout, stderr files
 Array[File] bco_tasks = []
 Array[File] stdout_tasks = []
 Array[File] stderr_tasks = []


 Array[Array[File]] bco_scatters = [bco_tasks]
 Array[Array[File]] stdout_scatters = [stdout_tasks]
 Array[Array[File]] stderr_scatters = [stderr_tasks]

 Array[File] bco_array = flatten(bco_scatters)
 Array[File] stdout_array = flatten(stdout_scatters)
 Array[File] stderr_array = flatten(stderr_scatters)

 call bco_merge_task.bco_merge {
   input:
       bco_array = bco_array,
       stdout_array = stdout_array,
       stderr_array = stderr_array,
       pipeline_name = pipeline_name,
       pipeline_version = pipeline_version
 }



  output {

    File stdout_log = bco_merge.stdout_log
    File stderr_log = bco_merge.stderr_log
    File bco = bco_merge.bco

  }

}
