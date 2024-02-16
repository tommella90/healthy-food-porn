#%%
import json 
import os
os.listdir("recipes/1._coconut_tamarind_salmon_curry")

#%%
# Generate HTML
def generate_recipe_html(recipe_data):
    html_content = f'''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>{recipe_data["name"]}</title>
        <!-- Add your CSS links here -->
    </head>
    <body>
        <section>
            <div>
                <h1 class="recipe-name">{recipe_data["name"]}</h1>
                <p class="recipe-time">{recipe_data["time"]} min</p>
            </div>
            <div>
                <ul class="recipe-ingredients">
                    {''.join(f"<li>{ingredient}</li>" for ingredient in recipe_data["ingredients"])}
                </ul>
            </div>
            <div>
                <h2>Preparation</h2>
                <ol class="recipe-preparation">
                    {''.join(f"<li>{step}</li>" for step in recipe_data["preparation"])}
                </ol>
            </div>
            <p class="recipe-comments">Comments: {recipe_data["comments"]}</p>
            <p class="recipe-source">Source: <a href="{recipe_data["source"]}">Youtube</a></p>
        </section>
    </body>
    </html>
    '''
    return html_content

# %%
recipes = os.listdir("recipes")

for recipe in recipes:
    with open(f"recipes/{recipe}/recipe.json") as json_file:
        recipe_data = json.load(json_file)

    html_content = generate_recipe_html(recipe_data)

    with open(f"recipes/{recipe}/index.html", "w") as file:
        file.write(html_content)

# %%
