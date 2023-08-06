workflow task_name_TAG_workflow
{
  call task_name_TAG
}

task task_name_TAG {

  String task_name = "task_name_TAG"
  String task_version = "latest"
  Int? index
  String task_name_with_index = if defined(index) then task_name + "_" + index else task_name
  String docker_image = "intelliseqngs/ubuntu-minimal-22.04:1.0.0"

  command <<<
   set -e -o pipefail
   bash /intelliseqtools/bco-after-start.sh --task-name-with-index ${task_name_with_index}



   bash /intelliseqtools/bco-before-finish.sh --task-name ${task_name} \
                                              --task-name-with-index ${task_name_with_index} \
                                              --task-version ${task_version} \
                                              --task-docker ${docker_image}
  >>>

  runtime {

    docker: docker_image
    memory: "1G"
    cpu: 1
    maxRetries: 2

  }

  output {

    File stdout_log = stdout()
    File stderr_log = stderr()
    File bco = "bco.json"

  }

}
