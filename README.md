# Sentiment Analysis Web Application (SAWA)
![Web Application Screenshot](https://github.com/blancos-code/SAWA/assets/79577721/03b58763-c122-474a-a3b3-b5eaca9d7206)


SAWA is a Sentiment Analysis Web Application built using Flask, Python, HTML, CSS, and Bootstrap. The application allows users to input text and analyze the sentiment behind it, classifying it as positive, negative, or neutral. It also provides a history of the analyzed texts with the ability to delete individual history items.

## Features

- **User-friendly web interface**: A clean and intuitive interface for users to input text for sentiment analysis.
- **Sentiment Analysis**: Analyzes the sentiment of the input text and classifies it as positive, negative, or neutral.
- **History of Analyses**: Keeps a history of the texts that have been analyzed, along with their sentiment scores.
- **Delete History Items**: Users can delete individual history items.
- **Dark and Light Theme Toggle**: Users can toggle between dark and light themes. The theme preference is saved locally.
- **Responsive Design**: The application is responsive and works well on different devices.

## Getting Started

### Prerequisites

- Python 3
- Virtualenv (optional)

### Installation

1. Clone the repository:
git clone https://github.com/blancos-code/SAWA.git
cd sentiment-analysis-webapp


2. (Optional) Create and activate a virtual environment:
python -m venv myenv
source myenv/bin/activate # On Windows, use myenv\Scripts\activate


3. Install the required packages:
pip install Flask textblob SQLAlchemy


4. Run the Flask application:
python app.py



5. Visit `http://127.0.0.1:5000` in your web browser to see the application.

## Usage

1. Enter text into the text area on the web page.
2. Click the "Analyze" button.
3. The sentiment result (positive, negative, or neutral) will be displayed below the text area.
4. Use the lightbulb icon in the top right corner to toggle between dark and light themes.
5. The history section displays previously analyzed texts. You can delete individual history items by clicking the "x" button next to them.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or create issues if you find any bugs or have suggestions for improvements.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [TextBlob](https://textblob.readthedocs.io/en/dev/) for providing the sentiment analysis functionality.
- [Bootstrap](https://getbootstrap.com/) for the responsive design and styling.
- [Font Awesome](https://fontawesome.com/) for the icons used in the application.
