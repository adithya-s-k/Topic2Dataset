# Topic2Dataset

## 👋🏼Introduction
data collection and preprocessing can be time-consuming and resource-intensive tasks. Topic2Dataset ia an open source project that helps by automating dataset generation from specified topics and websites, eliminating manual data gathering and accelerating dataset creation timelines. This project mainly aims to curate datasets for Retrieval augmented Generation (RAG) and LLM finetuning.

## 🔑Key Features
- **Effortless Dataset Generation:** Generate datasets for pre-training, fine-tuning, and preference modeling with ease.
- **Tailored Instruction and Data:** Upload a document and receive customized instructions and data for fine-tuning models.
- **AI-Powered Scraping:** Live AI agent-based scrapers ensure relevance, accuracy, and up-to-date data extraction.
- **Time-Dependent Scraping:** Keep datasets fresh and relevant with time-dependent scraping capabilities.
- **Seamless Data Export:** Export datasets to S3 and other blob storage services effortlessly for further analysis and usage.
- **Insightful Summarization:** Receive answers to questions and insights relevant to the document's content for enhanced understanding.

### Getting Started

Demo Notebook:
[![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/)

## Python Setup🐍
Clone the repository
```
git clone https://github.com/adithya-s-k/topic2dataset
cd topic2dataset
```
Install Required Dependencies
```
pip install -r requirements.txt
```
Quick Start dataset generation
```
python generate.py --topic Clinical Trials --website ["https://www.ncbi.nlm.nih.gov/pmc/tools/openftlist/" , "https://clinregs.niaid.nih.gov/#"] --time_in_hrs 10 --output local
```

### Contributing

Topic2Dataset is open source. We welcome contributions and collaboration from the community! See the project page for ways to contribute.

### License

This project is licensed under the MIT License - see the [LICENSE](./LICENSE) file for details.

### Citing

If you use Topic2Dataset in your research, please cite the following paper:

```
@article{Topic2Dataset,
  title={Topic2Dataset: AI-Drive Dataset curation for RAG and Finetuning},
  author={Adithya S K},
  year={2023}
}
```

## Disclaimer
The resources, including code, data, and model weights, associated with this project are restricted for academic research purposes only and cannot be used for commercial purposes. The content produced by any version of WizardLM is influenced by uncontrollable variables such as randomness, and therefore, the accuracy of the output cannot be guaranteed by this project. This project does not accept any legal liability for the content of the model output, nor does it assume responsibility for any losses incurred due to the use of associated resources and output results.
