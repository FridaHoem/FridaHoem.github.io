import json
import re

def parse_pubs():
    pubs = []
    with open('raw_pubs.txt', 'r') as f:
        lines = f.readlines()
        
    for line in lines:
        line = line.strip()
        if not line: continue
        
        # Check for URL
        url_match = re.search(r'(https?://[^\s,]+)', line)
        url = url_match.group(0) if url_match else ""
        
        # Remove URL from line to avoid confusion in splitting?
        # Maybe not necessary if we split by colon carefully.
        
        parts = line.split(':', 1)
        if len(parts) > 1:
            authors = parts[0].strip()
            # Clean trailing punctuation from authors
            authors = re.sub(r'[\.,;:]+$', '', authors)
            rest = parts[1].strip()
        else:
            authors = "Frida Snilstveit Hoem et al."
            rest = line

        # Try to extract year from the end
        year_match = re.search(r'\b(20\d{2})[a-z]?\.?$', line)
        year = year_match.group(1) if year_match else "n.d."
        
        # Identify venue by known list or heuristics
        journals = [
            "Nature Communications", "Journal of Micropaleontology", "Palaeogeography", 
            "Climate of the Past", "Nature Geoscience", "Paleoceanography", 
            "Global and Planetary Change", "Earth and Planetary Science Letters",
            "Utrecht Studies in Earth Sciences", "Nature communications",
            "Proceedings of the International Ocean Discovery Program"
        ]
        
        venue = "Unknown Venue"
        title = rest
        
        for j in journals:
            if j in rest:
                venue = j
                # Split title from venue
                # Title usually comes before venue
                try:
                    title_cand = rest.split(j)[0].strip()
                    # cleanup trailing punctuation
                    title_cand = re.sub(r'[\.,;]+$', '', title_cand)
                    if len(title_cand) > 5: # Valid title length
                        title = title_cand
                except:
                    pass
                break
        
        # If no venue found, try comma split
        if venue == "Unknown Venue":
            parts = rest.split(',')
            if len(parts) > 1:
                title = parts[0].strip()
                # Guess venue is second part?
                if len(parts) > 2:
                     venue = parts[1].strip()

        pubs.append({
            "title": title,
            "authors": authors,
            "year": year,
            "venue": venue,
            "url": url,
            "eprint_url": ""
        })

    # Sort by year descending
    pubs.sort(key=lambda x: str(x['year']), reverse=True)
    
    with open('data/publications.json', 'w') as f:
        json.dump(pubs, f, indent=2)

if __name__ == '__main__':
    parse_pubs()
