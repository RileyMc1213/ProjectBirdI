import tweeds
import kivy
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen

class TweeDSApp(App):
    def build(self):
        self.screen_manager = ScreenManager()

        # Creating the Main Screen
        self.main_screen = Screen()
        layout = BoxLayout(orientation='vertical', spacing=10)

        # Creating a text input field for the user to enter a keyword to search for tweets
        keyword_input = TextInput(hint_text='Enter keywords to search for tweets...')
        layout.add_widget(keyword_input)

        # Creating a button to search for tweets by keyword
        tweets_button = Button(text='Search Tweets')
        tweets_button.bind(on_press=lambda x: self.display_tweets(keyword_input.text))
        layout.add_widget(tweets_button)

        # Adding the widgets to the layout
        layout.add_widget(Label(text="tweets"))
        self.result_label = Label()
        layout.add_widget(self.result_label)
        layout.add_widget(Label(text='Separate multiple keywords with commas'))
        self.main_screen.add_widget(layout)

        # Adding the Main Screen to the Screen Manager
        self.screen_manager.add_widget(self.main_screen)

        return self.screen_manager

    # Function to get tweets by keyword and display the result
    def display_tweets(self, keywords):
        keyword_list = keywords.split(',')
        query = tweeds.Query()
        query.search = keyword_list
        query.limit = 10
        query.verified = True
        tweets = tweeds.search(query)

        # Creating the Tweet Screen
        tweet_screen = Screen(name='tweets')
        layout = BoxLayout(orientation='vertical', spacing=10)

        # Creating a label to display the tweets
        tweet_label = Label(text=f'The tweets containing the keywords "{", ".join(keyword_list)}" are: {tweets}')
        layout.add_widget(tweet_label)

        # Creating a button to go back to the Main Screen
        back_button = Button(text='Back')
        back_button.bind(on_press=lambda x: self.screen_manager.remove_widget(tweet_screen))
        layout.add_widget(back_button)

        # Adding the widgets to the layout
        tweet_screen.add_widget(layout)

        # Adding the Tweet Screen to the Screen Manager
        self.screen_manager.add_widget(tweet_screen)

# Running the Kivy app
if __name__ == '__main__':
    app = TweeDSApp()
    app.run()
Footer
