import os
path = '/Users/kim/Desktop/projects/DSA'
def disk_usage(path):
    total = os.path.getsize(path)

    if os.path.isdir(path):
        for filename in os.listdir(path):
            childpath = os.path.join(path, filename)
            total += disk_usage(childpath)

    print(f'{total:<7}, {path}')
    return total

# disk_usage(path)