# PowerML Python Package

## Installation

    pip install powerml_app

## Authentication
You will need a PowerML key. To get a PowerML key, go to [https://powerml.co/](https://powerml.co/) and log in with your email. Contact our team if you are unable to log in and we'll add you!

Optional: To get an OpenAI key, go to [https://beta.openai.com/account/api-keys](https://beta.openai.com/account/api-keys).

## Configuration

You configure the `PowerML` class by passing in a dictionary like so:

    from powerml import PowerML
    config = {"powerml": {"key": "<POWERML-KEY>"}}
    powerml = PowerML(config)

Optional: Create a config file at `~/.powerml/configure.yaml` with your PowerML and OpenAI keys. Here's an example:

    powerml:
        key: "<POWERML-KEY>"
    openai:
        key: "<OPENAI-KEY>"

These are default keys for the `PowerML` class but will be overriden by any configuration dictionary passed into the class constructor.

## Usage

You can use the member functions of the PowerML class, `predict` and `fit`, to make predictions with the model and fit data to the model to improve and customize it. 

You can use `predict` to run any prompt off the bat:

    from powerml import PowerML

    powerml = PowerML()
    
    # Run base model
    myPrompt = "hello there"
    response = powerml.predict(prompt=myPrompt)

To fit data to the model, you can use `fit` as so:

    # Fit model to data
    myData = ["item2", "item3"]
    myModel = powerml.fit(myData)

To run this fitted model, you can use `predict` again, specifying the new model name:

    # Use new model
    myModelName = myModel["model_name"]
    response = powerml.predict(prompt=myPrompt, model=myModelName)


## PowerML Class

The `PowerML` class has member functions `fit` and `predict`.

### Predict

`predict` accepts the following arguments:

    def predict(self,
                prompt: str,
                model: str = "text-davinci-003",
                stop: str = "",
                max_tokens: int = 128,
                temperature: int = 0,
                ) -> str:

`predict` will return a string of the model's output.

`fit` accepts the following arguments:

    def fit(self,
            data: list[str],
            model: str = ""):

`fit` will return a dictionary object in the following format:

    {
        "model_id":"23",
        "project_id":"None",
        "user_id":"12",
        "job_id":"89",
        "model_name":"be894276039088c5f8db3f6bfaeb19953ed9ffe55f37a847a58f9fb320d307bc",
        "job_config":"{\"type\": \"prompt_tune\", \"model_name\": \"llama\"}",
        "prompt":"item2item3{{input}}",
        "creation_time":"2022-12-20 02:19:36.519260",
        "job":{
            "job_id":"89",
            "project_id":"None",
            "user_id":"12",
            "config":"{\"type\": \"prompt_tune\", \"model_name\": \"llama\"}",
            "status":"COMPLETED",
            "name":"be894276039088c5f8db3f6bfaeb19953ed9ffe55f37a847a58f9fb320d307bc",
            "metric":"None",
            "history":"None",
            "start_time":"2022-12-20 02:19:36.369450",
            "end_time":"2022-12-20 02:19:35.837668"
        }
    }
    

## ExtractTopicsModel Class

The `ExtractTopicsModel` class is an example class designed to extract topics from the prompt.

### Usage
To instantiate a `ExtractTopicsModel`.

    model = ExtractTopicsModel(topics)

To customize your `ExtractTopicsModel` instance, you can pass it examples and topics to fit.

    # Examples in json for the model to fit to, in the format:
    # [
    #    { "example": "Using VS here for my IDE", labels: ["vscode"] },
    #    { "example": "A dashboard on Chrome", labels: ["web", "dashboard"] },
    # ]
    examples = get_json_examples()

    # Topics, e.g. ["vscode", "web", "dashboard"]
    topics = get_list_of_topics()
    
    model.fit(examples, topics)

Now, you can run this model on new examples with `predict`:

    new_example = "Move invite teammates page to its own base route . per designs:   This PR just moves existing views around and adds a new base route (i.e. no new functionality)"
    
    example_topics = model.predict(new_example)

### Methods

`__init__` is defined as follows:

    def __init__(self, config={}, model_name=None):

`fit` is defined as follows:

    def fit(self, 
            examples: list[
                {"example": str, "labels": list[str]}
            ],
            topics: list[str],
            ):

where examples is a list of dictionaries with format `{"example": str, "labels": list[str]}`.

`predict` is defined as follows:

    def predict(self, prompt: str):

## CreateTopicsModel Class

The `CreateTopicsModel` class is an example class designed to generate topics from a list of data. This is a batch process and may take a few minutes.

### Usage

    docs = get_list_of_data()
    learn_topics = CreateTopicsModel()
    learn_topics.fit(docs, topic_type='one-word system components')
    topics = learn_topics.predict()

#### Usage with `ExtractTopicsModel`
Topics can be learned by `CreateTopicsModel`, then used in `ExtractTopicsModel`. 

First, get topics from `CreateTopicsModel`:
    
    docs = get_list_of_data()
    learn_topics = CreateTopicsModel()
    learn_topics.fit(docs, topic_type='one-word system components')
    topics = learn_topics.predict()

Then, use `ExtractTopicsModel` as you normally would (as above) to fit it to examples, and then predict on new examples:

    topic_model = ExtractTopicsModel()
    labeled_data = get_formatted_examples()
    topic_model.fit(labeled_data, topics)

    new_example = "Move invite teammates page to its own base route . per designs:   This PR just moves existing views around and adds a new base route (i.e. no new functionality)"
    new_example_topics = topic_model.predict(new_example)

### Methods

`__init__` is defined as follows:

    def __init__(
            self,
            config={},
            num_subsamples=87,
            max_output_tokens=256,):

`fit` is defined as follows:

    def fit(self, documents, topic_type):

where documents is a list of strings.

`predict` is defined as follows:

    def predict(self):

and returns a set of strings.

## WriteEmailModel Class
The `WriteEmailModel` class is an example class designed to generate emails from a subject. 

### Usage

    model = WriteEmailModel()
    email = model.predict("Toys'r'Us")

## ExtractMenuItemsModel Class
The `ExtractMenuItemsModel` class is an example class designed to generate orders from a conversation. 

### Usage

    model = ExtractMenuItemsModel()
    items = model.predict("1 Chicken Burrito")

## ForecastSequenceModel Class
The `ForecastSequenceModel` class is an example class designed to generate a numeric sequence from a title. 

### Usage

    model = ForecastSequenceModel()
    autocompletion = model.predict("Freakonomics Radio")

## AutocompleteSQLModel Class
The `AutocompleteSQLModel` class is an example class designed to generate sql completions from a prompt. 

### Usage

    model = AutocompleteSQLModel()
    model.fit(
        table_schemas=[
            "CREATE TABLE users ( id SERIAL PRIMARY KEY, first_name TEXT, last_name TEXT);"
        ],
        example_queries=[
            "SELECT * FROM users WHERE id=?"
        ])
    autocompletion = model.predict("select * from ")

## QuestionAnswerModel Class
The `QuestionAnswerModel` class is an example class designed to generate questions from study material. 

### Usage

    model = QuestionAnswerModel()
    note = "Greek Philosophy"
    examples = [
        {'note': note,
        'questions': [{'Q': "Who said 'The only true wisdom is in knowing you know nothing.'", 'A': 'Socrates'},
        {'Q': "Who said 'I am the wisest man alive, for I know one thing, and that is that I know nothing.'", 'A': 'Socrates'}]}
    ]
    model.fit(examples)
    num_questions = 1
    question_and_answer = model.predict(note, num_questions)

