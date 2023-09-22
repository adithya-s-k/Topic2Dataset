# Document-Instruct

### AI-Assisted Document Understanding through Tailored Instruction Fine-tuning

Document-Instruct is an open source project that allows users to rapidly adapt language models to new documents through automatic generation of tailored instructions. By leveraging the context of a given document, Document-Instruct creates specialized training data to finetune models for enhanced understanding.

With Document-Instruct, you can upload a PDF or text document and quickly obtain a finetuned model that excels at answering questions and extracting insights related to that document. This makes it easy to handle new domains and topics without requiring large curated datasets.

### Key Features

- Upload a document and generate tailored instructions and data for finetuning
- Finetune language models with context-specific data for each document 
- Answer questions and summarize insights relevant to the document's content
- Web interface for easy use and sharing of finetuned models
- Open source implementation of instruction generation and finetuning

### Getting Started

You can try out Document-Instruct right away with the provided Colab notebook:

[![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/)

Alternatively, check out the project page for instructions on local usage and contributing:

https://github.com/adithya-s-k/document-instruct

### Solving the cold-start problem

Out-of-the-box language models often struggle with new topics and documents without relevant training data. Document-Instruct overcomes this cold-start challenge by automatically creating instructions tailored to the document context for finetuning. This allows rapid adaptation with minimal data.

### Democratizing document understanding

By providing an easy way to specialize models for individual documents, Document-Instruct makes state-of-the-art language technology accessible for new domains. Anyone can leverage customized models for extracting information from their own documents.

### Contributing

Document-Instruct is fully open source. We welcome contributions and collaboration from the community! See the project page for ways to contribute.

### License

This project is licensed under the MIT License - see the [LICENSE](./LICENSE) file for details.

### Citing Document-Instruct

If you use Document-Instruct in your research, please cite the following paper:

```
@article{document-instruct,
  title={Document-Instruct: AI-Assisted Document Understanding through Tailored Instruction Fine-tuning},
  author={Your Name},
  journal={Conference on Neural Information Processing Systems (NeurIPS)},
  year={2023}
}
```

## Disclaimer
The resources, including code, data, and model weights, associated with this project are restricted for academic research purposes only and cannot be used for commercial purposes. The content produced by any version of WizardLM is influenced by uncontrollable variables such as randomness, and therefore, the accuracy of the output cannot be guaranteed by this project. This project does not accept any legal liability for the content of the model output, nor does it assume responsibility for any losses incurred due to the use of associated resources and output results.

### References

<!-- ## DocsLLAMA

wanted to test if fine tuning a OSS model on a documentation is better that using RAG -->
