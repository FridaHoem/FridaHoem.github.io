import json
import os
from scholarly import scholarly

AUTHOR_ID = "5Roso-0AAAAJ"

def fetch_publications():
    print(f"Fetching publications for author ID: {AUTHOR_ID}")
    try:
        author = scholarly.search_author_id(AUTHOR_ID)
        scholarly.fill(author, sections=['publications'])
        
        publications = []
        for pub in author['publications']:
            try:
                scholarly.fill(pub)
                
                # Extract citation info
                bib = pub.get('bib', {})
                
                entry = {
                    'title': bib.get('title', 'Unknown Title'),
                    'authors': bib.get('author', 'Unknown Author').replace(" and ", ", "), # Basic formatting
                    'year': bib.get('pub_year', 'n.d.'),
                    'venue': bib.get('journal') or bib.get('conference') or bib.get('publisher') or 'Preprint/Other',
                    'url': pub.get('pub_url', ''),
                    'eprint_url': pub.get('eprint_url', '')
                }
                
                # Start of simple filtering if needed, but for now we take all
                publications.append(entry)
                
            except Exception as e:
                print(f"Error processing publication title {pub.get('bib', {}).get('title')}: {e}")
                continue

        # Sort by year descending
        publications.sort(key=lambda x: int(x['year']) if str(x['year']).isdigit() else 0, reverse=True)
        
        output_dir = 'data'
        os.makedirs(output_dir, exist_ok=True)
        
        output_file = os.path.join(output_dir, 'publications.json')
        with open(output_file, 'w') as f:
            json.dump(publications, f, indent=2)
            
        print(f"Successfully saved {len(publications)} publications to {output_file}")

    except Exception as e:
        print(f"An error occurred: {e}")
        exit(1)

if __name__ == "__main__":
    fetch_publications()
