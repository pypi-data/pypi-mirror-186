{
    "name": "{{ name }}",
    "description": "{{ description }}",
    "mode": "{{mode.upper()}}",
    "metrics": [],
    "area": "{{area.upper()}}",
    "url": "docker://gitlab.alidalab.it:5000/alida/analytics/spark-client/3-2-1:1.0.1",
    "version": "1.0.0",
    "accessLevel": "PUBLIC",
    "framework": {
        "id": 5,
        "name": "Spark",
        "version": "3.2"
    },
    "properties": [
        {% for input_dataset in input_datasets %}
        {
            "description": {{json.dumps(input_dataset.description)}},
            "mandatory": true,
            "type": "application",
            "defaultValue": null,
            "value": null,
            "key": "input-dataset",
            "valueType": "STRING",
            "inputData": null,
            "outputData": null,
            "invisible": true
        },
		{
			"defaultValue": {{json.dumps(translation['column_types'][input_dataset.columns_type])}},
			"description": "Selected columns from table",
			"key": "input-columns",
			"type": "application",
			"mandatory": true,
			"valueType": "STRING",
			"value": null,
			"inputData": null,
			"outputData": null,
            "invisible": true
		},
        {% endfor %}
        {% for output_dataset in output_datasets %}
        {
            "description": {{json.dumps(output_dataset.description)}},
            "mandatory": true,
            "type": "application",
            "defaultValue": null,
            "value": null,
            "key": "output-dataset",
            "valueType": "STRING",
            "inputData": null,
            "outputData": null,
            "invisible": true
        },
        {% endfor %}
        {% for input_model in input_models %}
        {   
            "description": {{json.dumps(input_model.description)}},
            "mandatory": true,
            "type": "application",
            "defaultValue": null,
            "value": null,
            "key": "input-model",
            "valueType": "STRING",
            "inputData": null,
            "outputData": null,
            "invisible": true
        },
        {% endfor %}
        {% for output_model in output_models %}
        {   
            "description": {{json.dumps(output_model.description)}},
            "mandatory": true,
            "type": "application",
            "defaultValue": null,
            "value": null,
            "key": "output-model",
            "valueType": "STRING",
            "inputData": null,
            "outputData": null,
            "invisible": true
        },
        {% endfor %}
        {% if ports.values()|length>0 %}
        {   
            "description": "List of ports to expose.",
            "mandatory": false,
            "type": "application",
            "defaultValue": "{\"ports\":[{% for port in ports.values() %}{\"port\":\"{{port.number}}\", \"name\":\"{{port.name}}\", \"http_model\":\"{{port.http_model}}\", \"url\":{{json.dumps(None)}}},{% endfor %}]}",
            "value": null,
            "key": "portsToExpose",
            "valueType": "JSON",
            "inputData": null,
            "outputData": null,
            "invisible": false
        },
        {% endif %}
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
            "description": "Container image pull policy used when pulling images within Kubernetes. Valid values are Always, Never, and IfNotPresent.",
            "mandatory": false,
            "type": "static",
            "defaultValue": "Always",
            "value": null,
            "key": "spark.kubernetes.container.image.pullPolicy",
            "valueType": "STRING",
            "externalized": false,
            "uri": null
        },
        {
            "description": "the spark master",
            "mandatory": false,
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
            "mandatory": false,
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
            "mandatory": false,
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
            "mandatory": false,
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
            "mandatory": false,
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
            "mandatory": false,
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
            "mandatory": false,
            "type": "static",
            "defaultValue": null,
            "value": null,
            "key": "spark.kubernetes.namespace",
            "valueType": "STRING",
            "externalized": false,
            "uri": null
        },
        {
            "description": "The URL for HDFS service",
            "mandatory": false,
            "type": "static",
            "defaultValue": null,
            "value": null,
            "key": "hdfsUrl",
            "valueType": "STRING",
            "externalized": false,
            "uri": null
        }
    ],
    "metrics": []
}

