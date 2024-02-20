#%%
import json 

import os 
recipes_dirs = os.listdir("recipes")
recipes_dirs.sort()

html_content = ""
img = "/pf2.png"

#%%
for recipe in recipes_dirs:
    print(recipe)

    directory = "recipes/" + recipe
    json_file = directory + "/recipe.json"
    # main_image = dir + "/main_image/main_image.jpg"
    img = "./pf2.png"
    with open(json_file) as json_file:
        recipe_json = json.load(json_file)


    # update html_content with the new recipe
    card = f"""

    <div class="container">
      <div class="row row-cols-1 row-cols-md-3 g-3">
        <div class="col">
          <div class="card shadow-sm">
            <img class="bd-placeholder-img card-img-top" width="100%" height="225" src="{img}" alt="Recipe Image">
            <div class="card-body">
              <p class="card-text">{recipe_json['name']}</p>
              <a href="./recipes/{recipe}/index.html">recipe</a>
              <div class="d-flex justify-content-between align-items-center">
                </div>
                <small class="text-body-secondary">{recipe_json['time']} min</small>
              </div>
            </div>
          </div>
        </div>
    """

    html_content += card
    print(html_content)

# save html_content to a file
path_to_save = "index_recipes.html"
with open(path_to_save, "w") as file:
    file.write(html_content)


    
# %%
