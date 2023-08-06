from powerml import Generator
from powerml import CreateTopicsModel
import nltk
from nltk.stem import WordNetLemmatizer

unblocked_human_unprompted_1gram_topics = [
    "SourceMarks",
    "VSCode",
    "Web",
    "Dashboard",
    "Kotlin",
    "Styles",
    "Services",
    "Video",
    "Messages",
    "Threads",
    "Mentions",
    "Git",
    "GitHub",
    "Auth",
    "Hub",
    "Slack",
    "Webhooks",
    "Gradle",
    "Intercom",
    "Adminconsole",
    "Ingestion",
    "Api",
    "Onboarding",
    "Discussions",
    "Insights",
    "Email",
    "Teams",
    "Notifications",
    "Pusher",
    "Logging",
    "Security",
    "Commands",
    "Controllers",
    "Stores",
    "Datastores",
    "Test",
    "Typescript",
    "React",
    "Recommendations",
    "Logs",
    "Compression",
    "Compute",
    "Webpack",
    "Webextension"]


class TopicGenerator(Generator):
    '''
    This is a class that can be used to generate more messages for CreateTopicsModels.
    '''

    def __init__(self, gold_topics=unblocked_human_unprompted_1gram_topics):
        nltk.download('wordnet')
        self.lemmatizer = WordNetLemmatizer()
        super().__init__([self.lemmatizer.lemmatize(topic.lower())
                          for topic in gold_topics])

    def _fit_and_predict(self, model, messages, _):
        model.fit(messages, 'one-word system components')
        generated_topics = [self.lemmatizer.lemmatize(
            topic.lower()) for topic in model.predict()]
        return generated_topics

    def _get_modifier(self, topic):
        return f'include the topic \'{topic}\''

    def get_rare(self, messages, return_metrics=True):
        """
        Parameters
        ----------
        messages: list[str]
            List of messages
        return_metrics: bool
            If True, return metrics

        Returns
        generated_data : The generated list of messages
        metrics (optional): Metrics on data coverage before and after generating messages
        -------
        """
        return super().get_rare(messages, return_metrics, CreateTopicsModel())
