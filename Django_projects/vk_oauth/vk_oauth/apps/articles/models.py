from django.db import models


class Article(models.Model):
	article_title = models.CharField('название статьи', max_length=200)  # VarChar in MySQL - 200-300 simbols?
	article_text = models.TextField('текст статьи')
	pub_date = models.DateTimeField('дата публикации')


class Comment(models.Model):
	article = models.ForeignKey(Article, on_delete=models.CASCADE)  #on_delete - delete all its comments if delete article
	author_name = models.CharField('имя автора', max_length=50)
	comment_text = models.CharField('текст комментария', max_length=200)
