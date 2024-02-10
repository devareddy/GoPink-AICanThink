import cohere

import os
import codecs

directory_path = 'dcis'

documents = []

for filename in os.listdir(directory_path):
    if filename.endswith(".txt"):  
        filepath = os.path.join(directory_path, filename)
        try:
            with codecs.open(filepath, 'r', encoding='utf-8') as file:
                content = file.read()
                
                document = {
                    "title": filename.replace('.txt', ''),  
                    "snippet": content
                }
                documents.append(document)
        except Exception as e:
            print(f"Error reading {filename}: {e}")


#Long-term survival of women with basal-like ductal carcinoma in situ of the breast
#MRI for diagnosis of pure ductal carcinoma in situ
#Effect of tamoxifen and radiotherapy in women with locally excised ductal carcinoma in situ
co = cohere.Client('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')
response = co.chat(
    message="Effect of tamoxifen and radiotherapy in women with locally excised ductal carcinoma in situ",
    documents=documents,
    prompt_truncation="AUTO"
)
print(response)
