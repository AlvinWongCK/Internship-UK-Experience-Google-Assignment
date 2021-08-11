"""A video player class."""

from .video_library import VideoLibrary
import random

# Global Variables to be used by some functions
isVideoPlaying = False  
isVideoPaused = False
currentVideoTitle = "Null"
currentVideoDetails = "Null"
user_playlist = []
user_flaglist = []

class VideoPlayer:
    """A class used to represent a Video Player."""

    def __init__(self):
        self._video_library = VideoLibrary()
        global isVideoPaused
        global isVideoPlaying
        global currentVideoTitle
        global currentVideoDetails
        global user_playlist
        global user_flaglist

        isVideoPlaying = False
        isVideoPaused = False
        currentVideoDetails = "Null"
        currentVideoTitle = "Null"
        user_playlist = []
        user_flaglist = []

    def number_of_videos(self):
        num_videos = len(self._video_library.get_all_videos())
        print(f"{num_videos} videos in the library")

    def show_all_videos(self):
        """Returns all videos."""

        global user_flaglist

        video_list = self._video_library.get_all_videos()
        video_list.sort(key =lambda x:x.title)
        
        print("Here's a list of all available videos:")
        for video in video_list:
            if len(user_flaglist) > 0:
                for flag_video in user_flaglist:
                    if video == flag_video[0]:
                        print(f'    {video.title} ({video.video_id}) [{" ".join(video.tags)}] - FLAGGED (reason: {flag_video[1]})')
                    else:
                        print(f'    {video.title} ({video.video_id}) [{" ".join(video.tags)}]')
            else:
                print(f'    {video.title} ({video.video_id}) [{" ".join(video.tags)}]')

    def play_video(self, video_id):
        """Plays the respective video.

        Args:
            video_id: The video_id to be played.
        """

        """
            Using Global variables to store a boolean value to check if any video is current playing
            Another global variable to store the title of the current video being played
        """
        global isVideoPlaying
        global isVideoPaused
        global currentVideoTitle
        global currentVideoDetails
        global user_flaglist
        
        video = self._video_library.get_video(video_id)

        if len(user_flaglist) > 0:
            for videos in user_flaglist:
                if video_id == videos[0].video_id:
                    return print(f"Cannot play video: Video is currently flagged (reason: {videos[1]})")

        if isVideoPlaying is False:
            if video is None:
                return print("Cannot play video: Video does not exist")
            else:
                isVideoPlaying = True
                currentVideoTitle = video.title
                currentVideoDetails = f'{video.title} ({video.video_id}) [{" ".join(video.tags)}]'
                return print(f"Playing video: {video.title}")
                
        else:
            if video is None:
                return print("Cannot play video: Video does not exist")
            else:
                if isVideoPaused is True:
                    isVideoPaused = False
                print(f"Stopping video: {currentVideoTitle}")
                currentVideoTitle = video.title
                currentVideoDetails = f'{video.title} ({video.video_id}) [{" ".join(video.tags)}]'
                return print(f"Playing video: {currentVideoTitle}")
                


    def stop_video(self):
        """Stops the current video."""

        global isVideoPlaying
        global currentVideoTitle
        global currentVideoDetails

        if isVideoPlaying is True:
            print(f"Stopping video: {currentVideoTitle}")
            isVideoPlaying = False
            currentVideoTitle = "Null"
            currentVideoDetails = "Null"
        else:
            print("Cannot stop video: No video is currently playing")


    def play_random_video(self):
        """Plays a random video from the video library."""

        global isVideoPlaying
        global currentVideoTitle
        global currentVideoDetails
        global user_flaglist

        temp_list = []
        for videos in self._video_library.get_all_videos():
            temp_list.append(videos)

        if len(user_flaglist) > 0:
            for video in user_flaglist:
                if video[0] in temp_list:
                    temp_list.remove(video[0])
        
        if len(temp_list) == 0:
            return print("No videos available")

        if isVideoPlaying is True:
            print(f"Stopping video: {currentVideoTitle}")
            randomVideo = random.choice(temp_list)
            print(f"Playing video: {randomVideo.title}")
            currentVideoTitle = randomVideo.title
            currentVideoDetails = f'{randomVideo.title} ({randomVideo.video_id}) [{" ".join(randomVideo.tags)}]'
        else:
            randomVideo = random.choice(temp_list)
            print(f"Playing video: {randomVideo.title}")
            isVideoPlaying = True
            currentVideoTitle = randomVideo.title
            currentVideoDetails = f'{randomVideo.title} ({randomVideo.video_id}) [{" ".join(randomVideo.tags)}]'

    def pause_video(self):
        """Pauses the current video."""

        global isVideoPlaying
        global currentVideoTitle
        global isVideoPaused

        if isVideoPlaying is True:
            if isVideoPaused is False:
                print(f"Pausing video: {currentVideoTitle}")
                isVideoPaused = True
            else:
                print(f"Video already paused: {currentVideoTitle}")
        else:
            print("Cannot pause video: No video is currently playing")

    def continue_video(self):
        """Resumes playing the current video."""

        global isVideoPlaying
        global currentVideoTitle
        global isVideoPaused

        if isVideoPlaying is False:
            print("Cannot continue video: No video is currently playing")
        else:
            if isVideoPaused is True:
                print(f"Continuing video: {currentVideoTitle}")
                isVideoPaused = False
            else:
                print("Cannot continue video: Video is not paused")


    def show_playing(self):
        """Displays video currently playing."""

        global isVideoPlaying
        global currentVideoDetails
        global currentVideoTitle
        global isVideoPaused

        if isVideoPlaying is True:
            if isVideoPaused is False:
                print(f"Currently playing: {currentVideoDetails}")
            else:
                print(f"Currently playing: {currentVideoDetails} - PAUSED")
        else:
            print("No video is currently playing")

    def create_playlist(self, playlist_name):
        """Creates a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """

        global user_playlist

        if len(user_playlist) < 1:
            print(f"Successfully created new playlist: {playlist_name}")
            temp_list = [playlist_name]
            user_playlist.append(temp_list)

        else:
            for x in user_playlist:
                if x[0].lower() == playlist_name.lower():
                    print("Cannot create playlist: A playlist with the same name already exists")
                    return
            print(f"Successfully created another new playlist: {playlist_name}")
            temp_list = [playlist_name]
            user_playlist.append(temp_list)

    def add_to_playlist(self, playlist_name, video_id):
        """Adds a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be added.
        """

        global user_playlist
        global user_flaglist

        counter = 0

        video = self._video_library.get_video(video_id)

        if len(user_flaglist) > 0:
            for videos in user_flaglist:
                if video_id == videos[0].video_id:
                    return print(f"Cannot add video to {playlist_name}: Video is currently flagged (reason: {videos[1]})")

        if len(user_playlist) < 1:
            print(f"Cannot add video to {playlist_name}: Playlist does not exist")
            return

        for x in user_playlist:
            if len(user_playlist) > 0:
                if x[0].lower() != playlist_name.lower():
                    counter += 1
                if counter == len(user_playlist):
                    print(f"Cannot add video to {playlist_name}: Playlist does not exist")
                    return

        if video is None:
            print(f"Cannot add video to {playlist_name}: Video does not exist")
            return
        
        for x in user_playlist:
            if len(x) > 1:
                if x[1].title == video.title:
                    print(f"Cannot add video to {playlist_name}: Video already added")
                    return

        for x in user_playlist:
            if x[0].lower() == playlist_name.lower():
                x.append(video)

        print(f"Added video to {playlist_name}: {video.title}")
                

    def show_all_playlists(self):
        """Display all playlists."""

        global user_playlist

        if len(user_playlist) < 1:
            print("No playlists exist yet")
            return
        
        user_playlist.sort(key =lambda x:x[0])

        print("Showing all playlists:")
        for playlist in user_playlist:
            print(f"    {playlist[0]}")


    def show_playlist(self, playlist_name):
        """Display all videos in a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        global user_playlist
        global user_flaglist
        counter = 0

        if len(user_playlist) == 0:
            return print(f"Cannot show playlist {playlist_name}: Playlist does not exist")

        for playlist in user_playlist:
            if playlist[0].lower() != playlist_name.lower():
                counter += 1
            if counter == len(user_playlist):
                return print(f"Cannot show playlist {playlist_name}: Playlist does not exist")

        for playlist in user_playlist:
            if playlist[0].lower() == playlist_name.lower():
                print(f"Showing playlist: {playlist_name}")
                if len(playlist) < 2:
                    print("    No videos here yet")
                else:
                    for videos in playlist[1:]:
                        if len(user_flaglist) > 0:
                            for flag_video in user_flaglist:
                                if videos == flag_video[0]:
                                    print(f"    {videos.title} ({videos.video_id}) [{' '.join(videos.tags)}] - FLAGGED (reason: {flag_video[1]})")
                                else:
                                    print(f"    {videos.title} ({videos.video_id}) [{' '.join(videos.tags)}]")
                        else:
                            print(f"    {videos.title} ({videos.video_id}) [{' '.join(videos.tags)}]")

    def remove_from_playlist(self, playlist_name, video_id):
        """Removes a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be removed.
        """

        global user_playlist
        video = self._video_library.get_video(video_id)
        counter = 0
        counter_2 = 0

        if len(user_playlist) == 0:
            return print(f"Cannot remove video from {playlist_name}: Playlist does not exist")

        for playlist in user_playlist:
            if playlist[0].lower() != playlist_name.lower():
                counter += 1
            elif playlist[0].lower() == playlist_name.lower():
                if video is None:
                    print(f"Cannot remove video from {playlist_name}: Video does not exist")
                else:
                    if len(playlist) > 1:
                        for videos in playlist[1:]:
                            if videos.video_id.lower() == video_id.lower():
                                print(f"Removed video from {playlist_name}: {videos.title}")
                                playlist.remove(videos)
                                return
                            elif videos.video_id.lower() != video_id.lower():
                                counter_2 += 1
                                print(counter_2)
                            
                            if counter_2 == len(playlist)-1:
                                return print(f"Cannot remove video from {playlist_name}: Video is not in playlist")
                    else:
                        return print(f"Cannot remove video from {playlist_name}: Video is not in playlist")

            if counter == len(user_playlist):
                return print(f"Cannot remove video from {playlist_name}: Playlist does not exist")
                


    def clear_playlist(self, playlist_name):
        """Removes all videos from a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """

        global user_playlist
        counter = 0

        if len(user_playlist) == 0:
            return print(f"Cannot clear playlist {playlist_name}: Playlist does not exist")

        for playlist in user_playlist:
            if playlist[0].lower() == playlist_name.lower():
                del playlist[1:]
                return print(f"Successfully removed all videos from {playlist_name}")
            else:
                counter += 1
            
            if counter == len(user_playlist):
                return print(f"Cannot clear playlist {playlist_name}: Playlist does not exist")

                
        

    def delete_playlist(self, playlist_name):
        """Deletes a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """

        global user_playlist
        counter = 0

        if len(user_playlist) == 0:
            return print(f"Cannot delete playlist {playlist_name}: Playlist does not exist")

        for playlist in user_playlist:
            if playlist[0].lower() == playlist_name.lower():
                user_playlist.remove(playlist)
                return print(f"Deleted playlist: {playlist_name}")
            else:
                counter += 1
            
            if counter == len(user_playlist):
                return print(f"Cannot delete playlist {playlist_name}: Playlist does not exist")


    def search_videos(self, search_term):
        """Display all the videos whose titles contain the search_term.

        Args:
            search_term: The query to be used in search.
        """

        global user_flaglist
        video_lib = self._video_library.get_all_videos()
        temp_list = []
        counter = 0
        index = 0

        for video in video_lib:
            if video.title.lower().find(search_term.lower()) != -1:
                temp_list.append(video)
            else:
                counter += 1
            
        if counter == len(video_lib):
            return print(f"No search results for {search_term}")

        print(f"Here are the results for {search_term}: ")
        temp_list.sort(key =lambda x:x.title)
        for vid in temp_list:
            if len(user_flaglist) > 0:
                for flag_video in user_flaglist:
                    if vid == flag_video[0]:
                        continue
                    else:
                        print(f'    {index+1}) {vid.title} ({vid.video_id}) [{" ".join(vid.tags)}]')
                        index += 1
            else:
                print(f'    {index+1}) {vid.title} ({vid.video_id}) [{" ".join(vid.tags)}]')
                index += 1
        
        print("Would you like to play any of the above? If yes, specify the number of the video.")
        print("If your answer is not a valid number, we will assume it's a no.")
        temp_val = input()

        try:
            val = int(temp_val)
        except ValueError:
            return

        while index != 0:
            if index == int(temp_val):
                return self.play_video(temp_list[int(temp_val)-1].video_id)

            
            index -= 1

        return
        

    def search_videos_tag(self, video_tag):
        """Display all videos whose tags contains the provided tag.

        Args:
            video_tag: The video tag to be used in search.
        """

        global user_flaglist
        video_lib = self._video_library.get_all_videos()
        temp_list = []
        counter = 0
        index = 0

        for video in video_lib:
            if video_tag.lower() in video.tags:
                temp_list.append(video)
                continue
            else:
                counter += 1
            
        if counter == len(video_lib):
            return print(f"No search results for {video_tag}")

        print(f"Here are the results for {video_tag}: ")
        temp_list.sort(key =lambda x:x.title)
        for vid in temp_list:
            if len(user_flaglist) > 0:
                for flag_video in user_flaglist:
                    if vid == flag_video[0]:
                        continue
                    else:
                        print(f'    {index+1}) {vid.title} ({vid.video_id}) [{" ".join(vid.tags)}]')
                        index += 1
            else:
                print(f'    {index+1}) {vid.title} ({vid.video_id}) [{" ".join(vid.tags)}]')
                index += 1
        
        print("Would you like to play any of the above? If yes, specify the number of the video.")
        print("If your answer is not a valid number, we will assume it's a no.")
        temp_val = input()

        try:
            val = int(temp_val)
        except ValueError:
            return

        while index != 0:
            if index == int(temp_val):
                return self.play_video(temp_list[int(temp_val)-1].video_id)

            index -= 1
        
        return 

    def flag_video(self, video_id, flag_reason=""):
        """Mark a video as flagged.

        Args:
            video_id: The video_id to be flagged.
            flag_reason: Reason for flagging the video.
        """
        global user_flaglist
        global isVideoPlaying
        global isVideoPaused
        global currentVideoTitle
        video = self._video_library.get_video(video_id)

        if video is None:
            return print(f"Cannot flag video: Video does not exist")

        if flag_reason == "":
            flag_reason = "Not supplied"

        if len(user_flaglist) > 0:
            for videos in user_flaglist:
                if video_id.lower() == videos[0].video_id.lower():
                    return print(f"Cannot flag video: Video is already flagged")

        if isVideoPlaying == True or isVideoPaused == True:
            if currentVideoTitle == video.title:
                self.stop_video()
        
        print(f"Successfully flagged video: {video.title} (reason: {flag_reason})")
        temp_list = [video, flag_reason]
        user_flaglist.append(temp_list)
        return
        

    def allow_video(self, video_id):
        """Removes a flag from a video.

        Args:
            video_id: The video_id to be allowed again.
        """

        global user_flaglist
        counter = 0
        video = self._video_library.get_video(video_id)

        if video is None:
            return print(f"Cannot remove flag from video: Video does not exist")

        for flag_video in user_flaglist:
            if video_id != flag_video[0].video_id:
                counter += 1
            else:
                print(f"Successfully removed flag from video: {flag_video[0].title}")
                user_flaglist.remove(flag_video)
                return

        if counter == len(user_flaglist):
            print(f"Cannot remove flag from video: Video is not flagged")

