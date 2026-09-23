def organize_hashtags(hashtags):
    unique_hashtags = set(hashtags)
    sorted_hashtags = sorted(unique_hashtags)
    return sorted_hashtags


hashtags = input("Enter hashtags separated by spaces: ").split()

organized_hashtags = organize_hashtags(hashtags)


print("\nOrganized Hashtags:")
for tag in organized_hashtags:
    print("#" + tag)

"""
---------------------------
After run:
education USA learning America history science college university USA AI STEM
"""