# Publish as a separate GitHub repository

Create an **empty** repository named `retail-sales-profit-powerbi` on https://github.com/new under account `MOHDTABISH78`; leave Initialize README unchecked.

Open the extracted `Retail_Sales_Project_1` folder in VS Code and use the terminal:

```bash
git init
git add .
git commit -m "Add synthetic retail sales analytics portfolio"
git branch -M main
git remote add origin https://github.com/MOHDTABISH78/retail-sales-profit-powerbi.git
git push -u origin main
```

You may need to sign into GitHub and set `git config --global user.name` and `git config --global user.email`. Do not confuse the ZIP with the project folder: extract it first.
