# rk-scraping-skills

1. Check Final_skill_data.csv
2. Run main.py.
3. Enter skills in manually.
4. Get new stackexchange skills (use 1K stackoverflow, 50 rest for now). Note you need to put at least 1 for both stackoverflow and the other sites.
5. Review new Final_skill_data.csv (change column width to 25)
6. Sync with production LD db.

- import_data.csv - original data from stackexchange (not used anymore)
- LD_site_data.csv - data from LD Site (not used anymore)

- new_data_from_stackexchange.csv - new data from stackexchange this round
- Final_skill_data.csv - final data for syncing with db

Original Project Guidelines: https://docs.google.com/document/d/11q0MhsHCefDnb-XW9RbC9guZTrWtSmngQ-OFTQzCzMI/edit

notes on filling:
cutoff of 1 on all sites
cutoff of 1 on stackoverflow