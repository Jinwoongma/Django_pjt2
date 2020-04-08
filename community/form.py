from django import forms
from .models import Review
from django.core.validators import MinValueValidator, MaxValueValidator

class ReviewForm(forms.ModelForm):
    title = forms.CharField(
                max_length=100,
                label='제목',
                help_text='제목은 100자이내로 작성하세요.',
                required=True,
                widget=forms.TextInput(
                        attrs={
                            'class': 'form-control',
                            'placeholder': '제목 입력',
                        }
                    )
            )

    movie_title = forms.CharField(
                max_length=30,
                label='영화 제목',
                help_text='영화제목은 30자이내로 작성하세요.',
                required=True,
                widget=forms.TextInput(
                        attrs={
                            'class': 'form-control',
                            'placeholder': '영화 제목 입력',
                        }
                    )
            )

    rank = forms.IntegerField(
                label='평점',
                required=True,
                help_text='1-5의 숫자를 작성해주세요.',
                validators=[MaxValueValidator(5), MinValueValidator(1)],
                widget=forms.NumberInput(
                        attrs={
                            'class': 'form-control',
                            'placeholder': '평점 입력',
                        }
                    )
            )

    content = forms.CharField(
                label='내용',
                help_text='자유롭게 작성해주세요.',
                required=True,
                widget=forms.Textarea(
                        attrs={
                            'row': 5,
                            'col': 50,
                        }
                    )
            )

    class Meta:
        model = Review
        fields = ['title', 'movie_title', 'rank', 'content']
