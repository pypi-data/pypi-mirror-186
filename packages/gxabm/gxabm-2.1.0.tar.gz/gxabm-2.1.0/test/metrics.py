import os
import sys
import json
import yaml
import bioblend.galaxy


job_index = {}

def load_config():
    path = os.path.expanduser("~/.abm/profile.yml")
    with open(path) as f:
        profiles = yaml.safe_load(f)
    return profiles


def record_job(data):
    cloud = data['cloud']
    if cloud not in job_index:
        job_index[cloud] = []
    job_index[cloud].append(data)


def process(filepath: str):
    with open(filepath) as f:
        job_data = json.load(f)
    job_id = os.path.basename(filepath).replace(".json", "")
    job_data['job_id'] = job_id
    record_job(job_data)
    # status = 'Yes' if 'job_metrics' in job_data['metrics'] else 'No'
    # print(filepath, job_data['cloud'], status)


def run(directories):
    for dir in directories:
        for file in os.listdir(dir):
            input_path = os.path.join(dir, file)
            if os.path.isfile(input_path) and input_path.endswith(".json"):
                process(input_path)

    profiles = load_config()
    for cloud,jobs in job_index.items():
        if cloud not in profiles:
            print(f"ERROR: cloud {cloud} has not been defined")
            continue
        profile = profiles[cloud]
        gi = bioblend.galaxy.GalaxyInstance(url=profile['url'], key=profile['key'])
        for job in jobs:
            id = job['metrics']['id']
            try:
                job['metrics']['job_metrics'] = gi.jobs.get_metrics(id)
                output_path = f"../resource-prediction/metrics/TestD-5-fixed/{id}.json"
                try:
                    with open(output_path, 'w') as f:
                        f.write(json.dumps(job, indent=4))
                    print(f"Wrote {output_path}")
                except Exception as e:
                    print(e)
            except:
                # print(f"Unable to get metrics for job {id} from {cloud}")
                pass

    # gi = bioblend.galaxy.GalaxyInstance()
    # data = gi.jobs.get_metrics('97af82a28609d22c')
    # print(json.dumps(data, indent=4))


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Please provide a directory name.")
    else:
        run(sys.argv[1:])