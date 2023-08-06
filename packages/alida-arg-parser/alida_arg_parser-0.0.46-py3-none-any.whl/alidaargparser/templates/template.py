{
    "name": "{{ name }}",
    "description": "{{ description }}",
    "mode": "{{mode.upper()}}",
    "area": "{{area.upper()}}",
    "url":  {{json.dumps(docker_image)}},
    "version": "1.0.0",
    "accessLevel": "PUBLIC",
    "framework": {
        "id": 6,
        "name": "Python",
        "version": "3",
        "imageUrl": "https://cdn.alidalab.it/static/images/frameworks/python_logo.png"
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
        {% if input_dataset.data_type == "table"  %}
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
        {% endif %}
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
            "defaultValue": "{\"ports\":[{% for port in ports.values() %}{\"port\":\"{{port.number}}\", \"name\":\"{{port.name}}\", \"http_model\":\"{{port.http_model}}\", \"url\":{{json.dumps(None)}}}{% if not loop.last %},{% endif %}{% endfor %}]}",
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
        {% if mode.upper() == "SINK" or mode.upper() == "PROCESSOR" %}
        {
            "description": "input topic name",
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
        {% endif %}
        {% if mode.upper() == "SOURCE" or mode.upper() == "PROCESSOR" %}
        {
            "description": "output topic name",
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
        {% endif %}
        {% if mode.upper() == "SOURCE" or mode.upper() == "PROCESSOR" or mode.upper() == "SINK" %}
        {
            "description": "Number of replicas",
            "mandatory": false,
            "defaultValue": "1",
            "value": null,
            "key": "replicas",
            "type": "tuning",
            "minValue": "1",
            "maxValue": "10",
            "measure": "NONE",
            "mappings": [],
            "category": false,
            "valueType": "INT"
        },
        {
            "description": "Memory request",
            "mandatory": false,
            "defaultValue": "200000000",
            "value": null,
            "key": "memoryRequest",
            "type": "tuning",
            "minValue": "100000000",
            "maxValue": "500000000",
            "measure": "BYTES",
            "mappings": [],
            "category": false,
            "valueType": "INT"
        },
        {% endif %}
    ],
    "metrics": []
}

