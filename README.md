# This branch is for testing purpose and not allowed to merge into main

## Get Started

### Create a New Virtual Environment:

1. With venv:

   ```bash
   # create environment
   python3.9 -m venv venv  #or other name you like

   # activate environment
   source venv/bin/activate    # macOS/Linux
   .\venv\Scripts\activate     # Windows
   ```

2. Or with conda:

   ```bash
   # create environment
   conda create -n yourEnvName python=3.9.18

   # activate environment
   conda activate yourEnvName
   ```

### Manage Dependencies:

- Install dependency:
  ```bash
  pip install -r requirements.txt
  ```
- Add new dependency:

  ```bash
  pip install <package-name>

  # commit in requirements.txt
  pip freeze > requirements.txt
  ```

### Start the programe

```bash
python3 scraper.py
```

## User Scraping

```python
person = Person("https://www.linkedin.com/in/joey-sham-aa2a50122", driver=driver, scrape=False)
```

- `scrape=False`: it doesn't automatically scrape the profile, but Chrome will open the linkedin page anyways.

```python
person.scrape(close_on_complete=False)
```

- when you run `person.scrape()`, it'll scrape and close the browser.
- `close_on_complete=False` make it do not close the browser

## URL

- The URL pattern should be `https://www.linkedin.com/in/joey-sham-aa2a50122` so I trim the strings after and include `?mini`
