from requests import get, post, delete


print(post('http://localhost:5000/api/v2/jobs', json={'job': 'cooking', 'work_size': 12,
                                                      'team_leader': 9, 'collaborators': '2, 4',
                                                      'is_finished': True, 'category': 3}).json())
print(get('http://localhost:5000/api/v2/jobs'))