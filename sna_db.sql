USE [SNA]
GO
/****** Object:  Table [dbo].[channel_data]    Script Date: 10/15/2023 10:06:07 AM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[channel_data](
	[Channel_id] [tinyint] NOT NULL,
	[Channel_name] [nvarchar](50) NOT NULL,
	[Subscribers] [int] NOT NULL,
	[Views] [int] NOT NULL,
	[Total_videos] [int] NOT NULL,
	[date] [date] NOT NULL
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[sentiment_data]    Script Date: 10/15/2023 10:06:07 AM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[sentiment_data](
	[comment_id] [int] NOT NULL,
	[video_id] [nvarchar](50) NOT NULL,
	[author_id] [nvarchar](max) NULL,
	[published_date] [date] NOT NULL,
	[sentiment] [float] NULL
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO
/****** Object:  Table [dbo].[video_data]    Script Date: 10/15/2023 10:06:07 AM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[video_data](
	[column1] [tinyint] NOT NULL,
	[Video_ID] [nvarchar](50) NOT NULL,
	[Title] [nvarchar](100) NOT NULL,
	[Published_date] [date] NOT NULL,
	[Views] [int] NOT NULL,
	[Likes] [smallint] NOT NULL,
	[Comments] [smallint] NOT NULL
) ON [PRIMARY]
GO
