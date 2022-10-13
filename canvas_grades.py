import json
import requests

bearer_token = # put token here
headerss = {'Authorization': f'Bearer {bearer_token}'}
user_id: int


# getting user id from a course response
course = requests.get('https://uncc.instructure.com/api/v1/courses/', headers=headerss)
course_resp = json.loads(course.text)
user_id = course_resp[0]['enrollments'][0]['user_id']
# can get user_id from above request's response and enrollments

def get_grades():
    course_enrolls = requests.get(f'https://uncc.instructure.com/api/v1/users/{user_id}/enrollments',headers=headerss)
    json_parsed = json.loads(course_enrolls.text)
    # iterating over each item in json response
    for x in range(len(json_parsed)):
        course_id = json_parsed[x]['course_id']
        course_api = requests.get(f'https://uncc.instructure.com/api/v1/courses/{course_id}', headers=headerss) # example course_id 154073
        course_json = json.loads(course_api.text)
        course_name: str = course_json['name']
        course_grade: str = str(json_parsed[x]['grades']['current_score'])
        # CCI pre-registration courses show up with null grade, so skipping those
        if course_grade == 'None':
            continue
        print(course_name, course_grade+"%", sep=" -----> ")
        print()


if __name__ == '__main__':
    get_grades()
