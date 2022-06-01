from time import sleep
from selenium import webdriver
import os, random
from Webscrapping.RedditPost import RedditPost
from moviepy.editor import *
from Utls.Picture import Picture
from sanitize_filename import sanitize
from PIL import Image
import shutil
from AWS import textToSpeech
from Webscrapping.SeleniumUtls import *

class Manager:
    def __init__(self):  
        self.audioPaths = []
        self.ImagePaths = []
        self.texts = []
        self.backgroundVideoPATH = os.getcwd() +  "\\Background_videos"
        self.finalVideosPATH = os.getcwd() +  "\\Final_Videos"
        self.postedVideosPATH = os.getcwd() +  "\\Final_Videos\\Posted"
        self.errorCount = 0
        self.currentTitle = None
        self.currentVideoPath = None
        self.currentVideoFilename = None
        self.subReddit = None

    def moveToPosted(self):
        toPath = self.finalVideosPATH + "\\" + self.postedVideosPATH
        shutil.move(self.currentVideoPath, toPath)

    def getSubredditFromLink(self, link):
        return link.split("/r/")[1].split("/")[0]

    def existsElement(self, xpath, driver):
        try:
            driver.find_element_by_xpath(xpath)
        except:
            return False
        return True

    # This gets the texts and images
    def getRedditStory(self, link):
        #TODO move images to image folder
        driver = self.getHeadlessDriverFireFox()
        driver.get(link)

        self.subReddit = self.getSubredditFromLink(link)

        xpath = "//button[contains(text(), 'Yes')]"
        xpath2 = "//button[contains(text(), 'Click to see nsfw')]"
        if self.existsElement(xpath, driver):
            driver.find_element_by_xpath(xpath).click()
            sleep(.5)
            if self.existsElement(xpath2, driver): 
                driver.find_element_by_xpath(xpath2).click()

        post = RedditPost(driver)
        self.currentTitle = post.getTitle()
        texts = [post.getTitle()] + post.getParagraphs()
        post.screenShotTitle()
        post.screenShotOfParagraphs()
        post.screenShotAwards()
        post.screenShotUpvotes()
        self.assembleTitleImage("Title.png")

        driver.close()
        imagePaths = []
        imagePaths.append("Title.png")
        for i in range(1, len(texts)):
            imagePaths.append(f"Paragraph{i}.png")
            self.ImagePaths.append(f"Paragraph{i}.png")
            i += 1
        return texts, imagePaths

    def getRedditTitleAndComments(self, link, limit):
        driver = webdriver.Chrome()
        driver.get(link)

        # Make a method inside reddit post
        xpath = "//button[contains(text(), 'Yes')]"
        xpath2 = "//button[contains(text(), 'Click to see nsfw')]"
        if self.existsElement(xpath, driver):
            driver.find_element_by_xpath(xpath).click()
            sleep(.5)
            if self.existsElement(xpath2, driver): 
                driver.find_element_by_xpath(xpath2).click()

        post = RedditPost(driver)
        self.currentTitle = post.getTitle()
        texts = [post.getTitle()] + post.getCommentsFullText(limit)
        post.screenShotTitle()
        post.screenShotOfComments(limit)

        driver.close()
        imagePaths = []
        imagePaths.append("Title.png")
        for i in range(1, len(texts)):
            imagePaths.append(f"Comment{i}.png")
            self.ImagePaths.append(f"Comment{i}.png")
            i += 1
        return texts, imagePaths

    # Where texts is a [] of strings, then gets audios
    def textToSpeech(self, texts):
        audioPaths = []
        i = 1
        for text in texts:
            fileName = f"audio{i}.mp3"
            textToSpeech(text, fileName)
            audioPaths.append(fileName)
            self.audioPaths.append(fileName)
            i += 1
        return audioPaths

    def createVideo(self, imagePaths, audioPaths, fileName):
        #TODO move video to final video folder
        # Grab backgroud video from background video folder
        self.concatenate_audio_moviepy(audioPaths, "combinedAudio.mp3")

        videoPath = self.backgroundVideoPATH + "\\" + self.choseRandomFileFromFolder(self.backgroundVideoPATH)
        videoclip = VideoFileClip(videoPath)
        audioclip = AudioFileClip("combinedAudio.mp3")
        new_audioclip = CompositeAudioClip([audioclip])
        videoclip.audio = new_audioclip
        print(new_audioclip.duration)

        # Resize image
        for path in imagePaths:
            pic = Picture(path)
            pic.resize(1.5)

        # Stich it all together
        i = 0
        currentTime = 0.0
        clipsToCat = []
        clipsToCat.append(videoclip)

        for audioPath in audioPaths:
            print(currentTime)
            audioclipTest = AudioFileClip(audioPath)

            print(f"{audioPath}, {audioclipTest.duration}")

            cat = (ImageClip(imagePaths[i])
                    .set_start(currentTime)
                    .set_duration(audioclipTest.duration)
                    .set_position(("center", "center")))

            clipsToCat.append(cat)
            currentTime += audioclipTest.duration
            i += 1
            audioclipTest.close()
        videoclip = CompositeVideoClip(clipsToCat)
        print(f"Now writing the video, there are {len(clipsToCat)} to cat")
        videoclip = videoclip.subclip(0, currentTime)
        print(f"File Name before sanitize: {fileName}")
        print(f"File Name after sanitize: {sanitize(fileName)}")
        finalPath = self.finalVideosPATH + "\\" + f"{sanitize(fileName)}.mp4"
        self.currentVideoFilename = f"{sanitize(fileName)}.mp4"

        #TODO SANATIZE THE FIlE NAME
        videoclip.write_videofile(finalPath, fps=24, threads=10)
        audioclip.close()
        new_audioclip.close()
        return finalPath

    # Returns true or false if it was sucessful or not
    def createTikTok(self, link):
        try:
            print("Getting screenshots and texts")
            texts, imagePaths = self.getRedditStory(link)
            
            print("Collecting Audios...")
            audioPaths = self.textToSpeech(texts)

            print("Creating video")
            self.currentVideoPath = self.createVideo(imagePaths, audioPaths, texts[0])

            print("Cleaning up")
            self.cleanUp(imagePaths, audioPaths)
            return True
        except Exception as e:
            print(e)
            self.errorCount += 1
            self.cleanUp(self.ImagePaths, self.audioPaths)
            return False

    ### Helper Methods ###
    def choseRandomFileFromFolder(self, folderPath):
        return random.choice(os.listdir(folderPath))
    
    def concatenate_audio_moviepy(self, audio_clip_paths, output_path):
        """Concatenates several audio files into one audio file using MoviePy
        and save it to `output_path`. Note that extension (mp3, etc.) must be added to `output_path`"""
        clips = [AudioFileClip(c) for c in audio_clip_paths]
        final_clip = concatenate_audioclips(clips)
        final_clip.write_audiofile(output_path)
        for clip in clips:
            clip.close()

    def removeFile(self, filePath):
        if os.path.exists(filePath):
            os.remove(filePath)
        else:
            print(f"FAILED TO DELETE: {filePath}, DID NOT EXSIST")
            self.errorCount += 1

    def cleanUp(self, imagesPaths, audioPaths):
        self.removeFile("combinedAudio.mp3")
        self.removeFile("Award.png")
        self.removeFile("Upvotes.png")
        self.removeFile(os.path.expanduser("~") + "\\Downloads\\narration.mp3")
        for path in imagesPaths:
            self.removeFile(path)
        for path in audioPaths:
            self.removeFile(path)
        self.ImagePaths = []
        self.audioPaths = []

    def get_concat_h(self, im1, im2):
        im1 = im1.resize((im1.width, im2.height))
        dst = Image.new('RGB', (im1.width + im2.width, im1.height))
        dst.paste(im1, (0, 0))
        dst.paste(im2, (im1.width, 0))
        return dst

    def get_concat_v(self, im1, im2):
        if im1.width < im2.width:
            dst = Image.new('RGB', (im1.width, im1.height + im2.height))
        else:
            dst = Image.new('RGB', (im2.width, im1.height + im2.height))
        dst.paste(im1, (0, 0))
        dst.paste(im2, (0, im1.height))
        return dst

    def assembleTitleImage(self, newPath):
        title = Image.open("Title.png")
        award = Image.open("Award.png")
        upvotes = Image.open("Upvotes.png")
        titleAndAward = self.get_concat_v(award, title)
        finalImage = self.get_concat_h(upvotes, titleAndAward)
        finalImage.save(newPath)

print(Manager.getSubredditFromLink("reddit.com/r/AmItheAsshole/top/?t=day"))