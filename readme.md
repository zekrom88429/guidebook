How to Contribute New Documentation to guidebook.

Welcome! To keep our documentation organized and ensure smooth deployment, please follow these steps when adding new pages.
1. Create a New File

Add your new .md file inside the docs/ folder (e.g., new-feature.md).
Naming Convention: Use lowercase letters and hyphens (e.g., project-guide.md). Avoid spaces and special characters.
Using the suffix of "en", "zh-Hans" and "zh-Hant" to lable different language versions.

2. Update the Navigation (```Nav```)
To make your new file appear in the sidebar, open the mkdocs.yml file in the root directory and add your file path under the nav section:

```nav:```<br>
```  - Home: index.md```<br>
```  - New Feature: new-feature.md```

3. Commit and Push
Once your changes are ready, push them to the repository:

Stage and commit your changes:
    ```git add .```
    ```git commit -m "docs: add documentation for [filename]"```

    ```Push to your branch:```
    ```git push origin [your-branch-name]```

    ```Open a Pull Request (PR):```
    ```Go to our GitHub repository and open a Pull Request to request a review from the team.```
