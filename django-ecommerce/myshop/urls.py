from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_view
from .forms import CustomerLoginForm,MyPasswordResetForm,PasswordResetConfirm,MyPasswordChangeForm, MySetPasswordForm,MyPasswordResetForm
urlpatterns=[
    path("",views.home, name='home'),
    path("category/", views.Category, name="category"),
    path("category/<slug:val>",views.CategoryView.as_view(), name="category"),
    path("product-detail/<int:pk>",views.ProductDetail.as_view(), name="product-detail"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    path("registration/", views.CustomerRegistrationView.as_view(), name="customerregistration"),
    path('accounts/login/', auth_view.LoginView.as_view(template_name="myshop/login.html",authentication_form=CustomerLoginForm), name='login'),
    path('profile/',views.ProfileView.as_view(), name="profile"),
    path('address/',views.address, name="address"),
    path('update-address/<int:pk>',views.UpdateAddress.as_view(), name="update-address"),
    path('changepassword/', auth_view.PasswordChangeView.as_view(template_name="myshop/changepassword.html", form_class=MyPasswordChangeForm, success_url='/passwordchangedone'), name="changepassword"),
    path('passwordchangedone',auth_view.PasswordChangeDoneView.as_view(template_name="myshop/passwordchangedone.html"),name="passwordchangedone"), 
    path('logout/',auth_view.LogoutView.as_view(next_page='login'), name="logout"),
    #cart details
    path('addtocart/',views.add_to_cart,name="addtocart"),
    path('cart',views.show_cart, name="showcart"),
    path('pluscart/',views.plus_cart),
    path('minuscart/',views.minus_cart),
    path('removecart/',views.remove_cart),
    path('checkout/',views.Checkout.as_view(), name="checkout"),


    #password reset
    path('password-reset/',auth_view.PasswordResetView.as_view(template_name="myshop/password-reset.html", form_class=MyPasswordResetForm), name="password-reset"),
    path('password-reset/done',auth_view.PasswordResetDoneView.as_view(template_name="myshop/password-reset-done.html"), name="password_reset_done"),
    path('password_reset_confirm/<uidb64>/<token>/',auth_view.PasswordResetConfirmView.as_view(template_name="myshop/password_reset_confirm.html", form_class=MySetPasswordForm), name="password_reset_confirm"),
    path('password-reset-complete/',auth_view.PasswordResetCompleteView.as_view(template_name="myshop/password-reset-complete.html"), name="password_reset_complete"),



]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)