<!-- add-breadcrumbs -->
# Video

**Videos can be added from both Vimeo and YouTube, using the Video DocType.**

You can add Videos with their URLs, descriptions, thumbnails, etc. Some of its uses are to maintain educational course material and to track personal YouTube video engagement.

To access Videos, go to:

> Home > Tools > Video

## 1. How to create a new Video

1. Go to the Video list and click on New.
2. Enter the title for the Video.
3. Select the Provider. The default Video Provider is YouTube.
4. Enter the URL to access the Video.
5. You can optionally add a publishing date and duration of the Video in days-hours-minutes-seconds.
6. You must also add some description for it.
7. Save.

After Saving, you will get a provision to add an image/thumbnail for the Video.
![Video](/docs/assets/img/education/video-after-save.png)

You can also watch the Video in the Document itself after saving it.
![Video](/docs/assets/img/education/video-watch.gif)

## 2. Features

### 2.1 Tracking Video Analytics via YouTube

YouTube Video statistics can be tracked and analysed. This is useful to track the view count and engagement of a Video you published.

For this you must first enable YouTube Tracking in **Video Settings**:
> Video Settings > Enable YouTube Tracking

Once you enable this, the **API Key** and **Frequency** fields will be visible.
![Video](/docs/assets/img/education/video-settings.png)

**API Key** : You can generate an API Key in your [Google Developers Console](https://console.developers.google.com/). You can refer to the [YouTube Data API Documentation](https://developers.google.com/youtube/v3/getting-started) for steps to generate the same.

**Frequency**: You can choose how often the system must automatically update your statistics. The available options are every 30 minutes, 1 hour, 6 hours and Daily (once everyday).

Apart from automatic updation, the statistics are updated on Save. So, all the Videos created/updated **after** enabling YouTube tracking, will have statistics updated on Save.
![Video](/docs/assets/img/education/video-stats.png)

### 2.2 YouTube Interactions Report

The YouTube Interactions Report provides a consolidated view of all the videos' engagements. The bar chart provides visual analysis of Likes vs Views.

You can filter the report data by the Published Date range.
![Video](/docs/assets/img/education/youtube-interactions.png)

> **Note** : The quota for the number of **non-billable** requests to the YouTube Data API is 10,000 requests as of September 2020. ERPNext automatically updates upto 50 videos in 1 request. Similarly, for 100 videos it would take 2 requests.<br>
Assuming 100 videos are updated **every hour** (frequency = 1 hour):<br>
>
- 2 requests will be sent per hour<br>
- 48 requests will be sent per a day<br>

> Please set the frequency accordingly.

{next}
