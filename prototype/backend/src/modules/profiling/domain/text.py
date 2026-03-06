from text_metrics.processor import extract

def fix_keys(data):
    if isinstance(data, dict):
        new_dict = {}
        for key, value in data.items():
            new_dict[str(key)] = fix_keys(value)
        return new_dict
    else:
        return data

def extract_metrics(text):
    metrics = extract(text)
    fixed_metrics = fix_keys(metrics)
    return fixed_metrics


VALIDATION_RULES = [
    { "group": "text", "metric": "lexicon_size", "min": 3, "max": 15 },
    { "group": "text", "metric": "symbols_length",  "max": 130  },
    { "group": "entities", "metric": "mean_usage_NUMBER",  "max": 2 },
    { "group": "entities", "metric": "mean_usage_ENUM",  "max": 0.4 },
    { "group": "entities", "metric": "mean_usage_MEAS",  "max": 0.4 },
    { "group": "entities", "metric": "mean_usage_FOREIGN",  "max": 1 },
]

def validate_metrics(metrics):
    validation_errors = []
    
    for rule in VALIDATION_RULES:
        group, name = rule['group'], rule['metric']
        
        metric_value = 0 if group not in metrics or name not in metrics[group] else metrics[group][name]
        
        if 'max' in rule and metric_value > rule['max']:
            validation_errors.append(f"{group}:{name} - Больше допустимого значения. {metric_value} > {rule['max']}")
            
        if 'min' in rule and metric_value < rule['min']:
            validation_errors.append(f"{group}:{name} - Меньше допустимого значения. {metric_value} < {rule['min']}")
            
    return validation_errors
