# ExaPy Search Tool

## Overview

This tool allows users to perform keyword searches using the ExaPy API, specifically targeting content on Instagram. The program retrieves the top five search results based on the provided query and displays the title and URL for each result. Additionally, the tool includes a feature to detect and notify users of any duplicate URLs in the search results.

## Features

- **Keyword Search:** Perform a search based on user input and retrieve relevant results from Instagram.
- **Duplicate Detection:** Check for duplicate URLs in the search results and notify the user if any are found.

## Installation

1. **Clone the Repository:**

   ```sh
   git clone https://github.com/your-repo/exa-py-search-tool.git
   ```

2. **Navigate to the Directory:**

   ```sh
   cd exa-py-search-tool
   ```

3. **Install Dependencies:**

   Ensure you have `exa_py` installed. You can install it using pip:

   ```sh
   pip install exa_py
   ```

   Also, ensure you have `requests` and `beautifulsoup4` installed:

   ```sh
   pip install requests beautifulsoup4
   ```

## Usage

1. **Run the Script:**

   ```sh
   python search_tool.py
   ```

2. **Enter a Search Query:**

   When prompted, input your search query:

   ```sh
   Search here: your search query
   ```

3. **View Results:**

   The script will display the title and URL of the top five search results. It will also notify you if any duplicate URLs are found.

## Example

Here is a sample interaction with the tool:

```
Search here: travel photos
Title: Stunning Sunset Over Mountains
URL: https://www.instagram.com/p/123456789

Title: Beautiful Beach
URL: https://www.instagram.com/p/987654321

Title: City Lights at Night
URL: https://www.instagram.com/p/111213141

Title: Serene Forest Path
URL: https://www.instagram.com/p/161718192

Title: Ocean Waves
URL: https://www.instagram.com/p/202122232

No duplicate URLs found.
```

## Contributing

Contributions are welcome! Please fork this repository and submit pull requests for any enhancements or bug fixes.


