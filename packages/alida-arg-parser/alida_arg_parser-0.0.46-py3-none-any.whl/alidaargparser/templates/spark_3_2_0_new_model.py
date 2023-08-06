{
    "name": "{{ name }}",
    "description": "{{ description }}",
    "mode": "{{mode.upper()}}",
    "metrics": [],
    "area": "{{area.upper()}}",
    "url": "docker://gitlab.alidalab.it:5000/alida/analytics/spark-client/3-2-1:1.0.1",
    "version": "1.0.0",
    "framework": {
        "id": 5,
        "name": "Spark",
        "version": "3.2"
    },
    "assets": { 
        "datasets": 
            {"input":[
                {% for input_dataset in input_datasets %}
                {   "name":{{json.dumps(input_dataset.name)}},
                    "description": {{json.dumps(input_dataset.description)}},
                    "type": "tabular",
                    "col_type": {{json.dumps(translation['column_types'][input_dataset.columns_type])}},
                    "order": {{loop.index-1}}
                },
                {% endfor %}
                ],
            "output": [
                {% for output_dataset in output_datasets %}
                {   "name":{{json.dumps(output_dataset.name)}},
                    "description": {{json.dumps(output_dataset.description)}},
                    "type": "tabular",
                    "order": {{loop.index-1}}
                },
                {% endfor %}
                ]
            },
        "models": 
            {"input":[
                {% for input_model in input_models %}
                {   "name":{{json.dumps(input_model.name)}},
                    "description": {{json.dumps(input_model.description)}},
                    "storage_type": "hdfs",
                    "order": {{loop.index-1}}
                },
                {% endfor %}
                ],
            "output": [
                {% for output_model in output_models %}
                {   "name":{{json.dumps(output_model.name)}},
                    "description": {{json.dumps(output_model.description)}},
                    "storage_type": "hdfs",
                    "order": {{loop.index-1}}
                },
                {% endfor %}
                ]
            }
    },
    "properties": [
        {% for property in properties %}
        {
            "description": {{json.dumps(property.description)}},
            "mandatory": {{json.dumps(property.required)}},
            "type": "application",
            "defaultValue": {{json.dumps(property.default)}},
            "value": null,
            "key": {{json.dumps(property.name)}},
            "valueType": {{json.dumps(translation['type'][property.type])}},
            "inputData": null,
            "outputData": null
        },
        {% endfor %}
        {
            "description": "Dataset delimiter",
            "mandatory": false,
            "type": "application",
            "defaultValue": ",",
            "value": null,
            "key": "delimiter",
            "valueType": "STRING",
            "inputData": false,
            "outputData": false
        },
        {
            "description": "Container image pull policy used when pulling images within Kubernetes. Valid values are Always, Never, and IfNotPresent.",
            "mandatory": true,
            "type": "static",
            "defaultValue": "Always",
            "value": null,
            "key": "spark.kubernetes.container.image.pullPolicy",
            "valueType": "STRING",
            "externalized": false,
            "uri": null
         },
        {
            "description": "Class to use for serializing objects that will be sent over the network or need to be cached in serialized form",
            "mandatory": false,
            "type": "tuning",
            "defaultValue": "0",
            "value": null,
            "key": "spark.serializer",
            "valueType": "INT",
            "minValue": "0",
            "maxValue": "1",
            "measure": "NONE",
            "mappings": [
                {
                    "intValue": 0,
                    "name": "org.apache.spark.serializer.JavaSerializer"
                },
                {
                    "intValue": 1,
                    "name": "org.apache.spark.serializer.KryoSerializer"
                }
            ],
            "category": true
        },
        {
            "description": "The codec used to compress internal data such as RDD partitions, event log, broadcast variables and shuffle outputs",
            "mandatory": false,
            "type": "tuning",
            "defaultValue": "0",
            "value": null,
            "key": "spark.io.compression.codec",
            "valueType": "INT",
            "minValue": "0",
            "maxValue": "2",
            "measure": "NONE",
            "mappings": [
                {
                    "intValue": 0,
                    "name": "lz4"
                },
                {
                    "intValue": 1,
                    "name": "lzf"
                },
                {
                    "intValue": 2,
                    "name": "snappy"
                }
            ],
            "category": true
            
        },
        {
            "description": "Maximum size of map outputs to fetch simultaneously from each reduce task",
            "mandatory": false,
            "type": "tuning",
            "defaultValue": "50331648",
            "value": null,
            "key": "spark.reducer.maxSizeInFlight",
            "valueType": "INT",
            "minValue": "25165824",
            "maxValue": "100663296",
            "measure": "BYTES",
            "mappings": [],
            "category": false
        
        },
        {
            "description": "Default number of partitions in RDDs returned by transformations like join, reduceByKey, and parallelize when not set by user",
            "mandatory": false,
            "type": "tuning",
            "defaultValue": "1",
            "value": null,
            "key": "spark.default.parallelism",
            "valueType": "INT",
            "minValue": "1",
            "maxValue": "16",
            "measure": "NONE",
            "mappings": [],
            "category": false
        },
        {
            "description": "Size of each piece of a block for TorrentBroadcastFactory",
            "mandatory": false,
            "type": "tuning",
            "defaultValue": "4194304",
            "value": null,
            "key": "spark.broadcast.blockSize",
            "valueType": "INT",
            "minValue": "2097152",
            "maxValue": "8388608",
            "measure": "BYTES",
            "mappings": [],
            "category": false
        
        },
        {
            "description": "Number of cores to allocate for each task",
            "mandatory": false,
            "type": "tuning",
            "defaultValue": "1",
            "value": null,
            "key": "spark.task.cpus",
            "valueType": "INT",
            "minValue": "1",
            "maxValue": "8",
            "measure": "NONE",
            "mappings": [],
            "category": false
        
        },
        {
            "description": "If set to true, performs speculative execution of tasks",
            "mandatory": false,
            "type": "tuning",
            "defaultValue": "0",
            "value": null,
            "key": "spark.speculation",
            "valueType": "BOOLEAN",
            "minValue": "0",
            "maxValue": "1",
            "measure": "NONE",
            "mappings": [],
            "category": false
        },
        {
            "description": "the spark master",
            "mandatory": true,
            "type": "static",
            "defaultValue": null,
            "value": null,
            "key": "spark.master",
            "valueType": "STRING",
            "externalized": false,
            "uri": null
        },
        {
            "description": "Spark app name",
            "mandatory": true,
            "type": "static",
            "defaultValue": "{{ name }}",
            "value": null,
            "key": "spark.name",
            "valueType": "STRING",
            "externalized": false,
            "uri": null
        },
        {
            "description": "Python module",
            "mandatory": true,
            "type": "static",
            "defaultValue": "main",
            "value": null,
            "key": "pythonModule",
            "valueType": "STRING",
            "externalized": false,
            "uri": null
        },
        {
            "description": "Number of executors",
            "mandatory": true,
            "type": "static",
            "defaultValue": 3,
            "value": null,
            "key": "spark.executor.instances",
            "valueType": "INT",
            "externalized": false,
            "uri": null
        },
        {
            "description": "Kubernetes secrets used to pull images from private image registries",
            "mandatory": true,
            "type": "static",
            "defaultValue": null,
            "value": null,
            "key": "spark.kubernetes.container.image.pullSecrets",
            "valueType": "STRING",
            "externalized": false,
            "uri": null
        },
        {
            "description": "Container image to use for the Spark application",
            "mandatory": true,
            "type": "static",
            "defaultValue": {{json.dumps(docker_image.replace("docker://", ""))}},
            "value": null,
            "key": "spark.kubernetes.container.image",
            "valueType": "STRING",
            "externalized": false,
            "uri": null
        },
        {
            "description": "The namespace that will be used for running the driver and executor pods",
            "mandatory": true,
            "type": "static",
            "defaultValue": null,
            "value": null,
            "key": "spark.kubernetes.namespace",
            "valueType": "STRING",
            "externalized": false,
            "uri": null
        },
        {
            "description": "Whether to compress map output files",
            "mandatory": false,
            "type": "tuning",
            "defaultValue": "1",
            "value": null,
            "key": "spark.shuffle.compress",
            "valueType": "BOOLEAN",
            "minValue": "0",
            "maxValue": "1",
            "measure": "NONE",
            "mappings": [],
            "category": false
        },
        {
            "description": "The URL for HDFS service",
            "mandatory": true,
            "type": "static",
            "defaultValue": null,
            "value": null,
            "key": "hdfsUrl",
            "valueType": "STRING",
            "externalized": false,
            "uri": null
        },
        {
            "description": "Whether to compress broadcast variables before sending them",
            "mandatory": false,
            "type": "tuning",
            "defaultValue": "1",
            "value": null,
            "key": "spark.broadcast.compress",
            "valueType": "BOOLEAN",
            "minValue": "0",
            "maxValue": "1",
            "measure": "NONE",
            "mappings": [],
            "category": false
    
        },
        {
            "description": "Whether to compress data spilled during shuffles",
            "mandatory": false,
            "type": "tuning",
            "defaultValue": "1",
            "value": null,
            "key": "spark.shuffle.spill.compress",
            "valueType": "BOOLEAN",
            "minValue": "0",
            "maxValue": "1",
            "measure": "NONE",
            "mappings": [],
            "category": false
        }
    ],
    "metrics": []
}

