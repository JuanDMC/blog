from django.shortcuts import render, redirect
from django.utils import timezone
from .models import Post
from django.shortcuts import render, get_object_or_404
from .forms import PostForm

# Create your views here.
def post_list(request):
    posts = Post.objects.order_by('fecha_publicado')
    return render(request, 'blog/post_list.html', {'posts': posts})
    

def detalle_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/detalle_post.html', {'post': post}) 

def nuevo_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
                post = form.save(commit=False)
                post.autor = request.user
                # post.fecha_publicado = timezone.now()
                post.save()
                return redirect('detalle_post', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/editar_post.html', {'form': form})

def editar_post(request, pk):
        post = get_object_or_404(Post, pk=pk)
        if request.method == "POST":
            form = PostForm(request.POST, instance=post)
            if form.is_valid():
                post = form.save(commit=False)
                post.autor = request.user
                post.save()
                return redirect('detalle_post', pk=post.pk)
        else:
            form = PostForm(instance=post)
        return render(request, 'blog/editar_post.html', {'form': form})

def lista_borradores(request):
    posts = Post.objects.filter(fecha_publicado__isnull=True).order_by('fecha_creado')
    return render(request, 'blog/lista_borradores.html', {'posts': posts})
