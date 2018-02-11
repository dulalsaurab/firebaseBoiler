from django import forms
from .models import postArticles
from mediumeditor.widgets import MediumEditorTextarea
# from ckeditor_uploader.widgets import CKEditorWidget, CKEditorUploadingWidget
class editorForms(forms.ModelForm):
    #meta tells which form to import
    class Meta:
        model = postArticles
        fields = ('title', 'shortInfo', 'text', 'tags')
        # text = forms.CharField(widget=CKEditorUploadingWidget())
        widgets = {
            'title': forms.TextInput(
                    attrs = {'class': 'form-control form-control-lg',
                            'placeholder': 'शीर्षक',
                        }
                    ),
             'text': forms.TextInput(
                    attrs = {
                            'class': 'django-ckeditor-widget',
                            'placeholder': 'write a big long text \n ',
                            'width': '100%',
                    }
                ),
             'tags': forms.TextInput(
                    attrs = {
                            'class': 'form-control',
                            'placeholder': '# enter your tags'

                        }
                    ),
             'shortInfo': forms.TextInput(
                           attrs = {
                                   'class': 'form-control',
                                   'placeholder': 'What \'s this article about?',
                           }
                    ),

            # 'text': forms.TextInput(
            #         attrs = {'class': 'form-group',
            #                 'id': 'editor',
            #                 'placeholder': '''यहाँ लेख्नुहोस्... \n
            #                      Some initial <strong>bold</strong> text
            #                      <p><br></p><br />'''
            #             },
            # ),
        }
        # your_name = forms.CharField(label='Your name', max_length=100)
