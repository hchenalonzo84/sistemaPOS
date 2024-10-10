from django.shortcuts import render, redirect
from django.views import generic
from django.urls import reverse_lazy
from django.contrib import messages

from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin

#Decoradores
from django.contrib.auth.decorators import login_required, permission_required

from .models import Categoria, SubCategoria, Marca, UnidadMedida, Producto
from .forms import CategoriaForm, SubCategoriaForm, MarcaForm, UnidadMedidaForm, ProductoForm

#Importar vista sin privilegios desde base
from bases.views import SinPrivilegios

class CategoriaView(SinPrivilegios, generic.ListView):
    permission_required = "inv.view_categoria"
    model = Categoria
    template_name = "inv/categoria_list.html"
    context_object_name = "obj"
    

class CategoriaNew(SuccessMessageMixin,SinPrivilegios, generic.CreateView): #Crear vista
    permission_required = "inv.view_categoria"
    model = Categoria
    template_name = "inv/categoria_form.html"
    context_object_name = "obj"
    form_class=CategoriaForm #Pasar formulario
    success_url=reverse_lazy("inv:categoria_list")
    success_message="Categoria Creada Satisfactoriamente"

    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)
    
class CategoriaEdit(SuccessMessageMixin,SinPrivilegios, generic.UpdateView): #Crear vista
    permission_required = "inv.view_categoria"
    model = Categoria
    template_name = "inv/categoria_form.html"
    context_object_name = "obj"
    form_class=CategoriaForm #Pasar formulario
    success_url=reverse_lazy("inv:categoria_list")
    success_message = "Categoria Editada Satisfactoriamente"

    def form_valid(self, form):
        form.instance.um = self.request.user.id
        return super().form_valid(form)
    
class CategoriaDelete(SuccessMessageMixin,SinPrivilegios, generic.DeleteView):
    permission_required = "inv.view_categoria"
    model = Categoria
    template_name = 'inv/catalogos_del.html'
    context_object_name = 'obj'
    success_url = reverse_lazy("inv:categoria_list")
    success_message = "Categoria Eliminada Satisfactoriamente"

class SubCategoriaView(SinPrivilegios, generic.ListView): #Crear vista SubCategoria
    permission_required = "inv.view_subcategoria"
    model = SubCategoria
    template_name = "inv/subcategoria_list.html"
    context_object_name = "obj"
    login_url = 'bases:login'


class SubCategoriaNew(SuccessMessageMixin,SinPrivilegios, generic.CreateView): 
    permission_required = "inv.view_subcategoria"
    model = SubCategoria
    template_name = "inv/subcategoria_form.html"
    context_object_name = "obj"
    form_class=SubCategoriaForm 
    success_url=reverse_lazy("inv:subcategoria_list")
    success_message = "Subcategoría Creada Satisfactoriamente"

    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)
    

class SubCategoriaEdit(SuccessMessageMixin,SinPrivilegios, generic.UpdateView):
    permission_required = "inv.view_subcategoria"
    model=SubCategoria
    template_name = "inv/subcategoria_form.html"
    context_object_name = "obj"
    form_class=SubCategoriaForm 
    success_url=reverse_lazy("inv:subcategoria_list")
    success_message = "Subcategoria Editada Satisfactoriamente"

    def form_valid(self, form):
        form.instance.um = self.request.user.id
        return super().form_valid(form)
    

class SubCategoriaDelete(SuccessMessageMixin,SinPrivilegios, generic.DeleteView):
    permission_required = "inv.view_subcategoria"
    model = SubCategoria
    template_name = 'inv/catalogos_del.html'
    context_object_name = 'obj'
    success_url = reverse_lazy("inv:subcategoria_list")
    success_message = "Subcategoria Eliminada Satisfactoriamente"


class MarcaView(SinPrivilegios, generic.ListView):
    permission_required = 'inv.view_marca'
    model = Marca
    template_name = "inv/marca_list.html"
    context_object_name = "obj"


class MarcaNew(SuccessMessageMixin,SinPrivilegios, generic.CreateView): 
    permission_required = 'inv.view_marca'
    model = Marca
    template_name = "inv/marca_form.html"
    context_object_name = "obj"
    form_class=MarcaForm 
    success_url=reverse_lazy("inv:marca_list")
    success_message = "Marca Creada Satisfactoriamente"

    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)


class MarcaEdit(SuccessMessageMixin,SinPrivilegios, generic.UpdateView):
    permission_required = 'inv.view_marca'
    model=Marca
    template_name = "inv/marca_form.html"
    context_object_name = "obj"
    form_class=MarcaForm 
    success_url=reverse_lazy("inv:marca_list")
    success_message = "Marca Editada Satisfactoriamente"

    def form_valid(self, form):
        form.instance.um = self.request.user.id
        return super().form_valid(form)

@login_required(login_url = '/login/')
@permission_required('inv.change_marca', login_url='bases:sin_privilegios')
def marca_inactivar(request, id):
    marca = Marca.objects.filter(pk=id).first()
    contexto={}
    template_name="inv/catalogos_del.html"

    if not marca:
        return redirect("inv:marca_list")
    
    if request.method=='GET':
        contexto={'obj':marca}

    if request.method=='POST':
        marca.estado=False
        marca.save()
        messages.success(request, 'Marca Inactivada')
        return redirect("inv:marca_list")

    return render(request,template_name,contexto)


class UnidadMedidaView(SuccessMessageMixin,SinPrivilegios, generic.ListView):
    permission_required = 'inv.unidadmedida'
    model = UnidadMedida
    template_name = "inv/unidadmedida_list.html"
    context_object_name = "obj"


class UnidadMedidaNew(SuccessMessageMixin,SinPrivilegios, generic.CreateView): 
    permission_required = 'inv.unidadmedida'
    model = UnidadMedida
    template_name = "inv/unidadmedida_form.html"
    context_object_name = "obj"
    form_class=UnidadMedidaForm 
    success_url=reverse_lazy("inv:unidadmedida_list")
    login_url='bases:login'
    success_message = "Unidad de Medidad Creada Satisfactoriamente"

    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)


class UnidadMedidaEdit(SuccessMessageMixin,SinPrivilegios, generic.UpdateView):
    permission_required = 'inv.unidadmedida'
    model=UnidadMedida
    template_name = "inv/unidadmedida_form.html"
    context_object_name = "obj"
    form_class=UnidadMedidaForm 
    success_url=reverse_lazy("inv:unidadmedida_list")
    login_url='bases:login'
    success_message = "Unidad de Medidad Editada Satisfactoriamente"

    def form_valid(self, form):
        form.instance.um = self.request.user.id
        print(self.request.user.id)
        return super().form_valid(form)

@login_required(login_url = '/login/')
@permission_required('inv.change_unidadmedida', login_url='bases:sin_privilegios')
def unidadmedida_inactivar(request, id):
    um = UnidadMedida.objects.filter(pk=id).first()
    contexto={}
    template_name="inv/catalogos_del.html"

    if not um:
        return redirect("inv:unidadmedida_list")
    
    if request.method=='GET':
        contexto={'obj':um}

    if request.method=='POST':
        um.estado=False
        um.save()
        return redirect("inv:unidadmedida_list")
    
    return render(request,template_name,contexto)


class ProductoView(SinPrivilegios, generic.ListView):
    permission_required = 'inv.producto'
    model = Producto
    template_name = "inv/producto_list.html"
    context_object_name = "obj"


class ProductoNew(SuccessMessageMixin,LoginRequiredMixin, generic.CreateView): 
    model = Producto
    template_name = "inv/producto_form.html"
    context_object_name = "obj"
    form_class=ProductoForm
    success_url=reverse_lazy("inv:producto_list")
    login_url='bases:login'
    success_message = "Producto Creado Satisfactoriamente"

    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super(ProductoNew, self).get_context_data(**kwargs)
        context["categorias"] = Categoria.objects.all()
        context["subcategorias"] = SubCategoria.objects.all()
        return context

class ProductoEdit(SuccessMessageMixin,LoginRequiredMixin, generic.UpdateView):
    model=Producto
    template_name = "inv/producto_form.html"
    context_object_name = "obj"
    form_class=ProductoForm 
    success_url=reverse_lazy("inv:producto_list")
    login_url='bases:login'
    success_message = "Producto Editado Satisfactoriamente"

    def form_valid(self, form):
        form.instance.um = self.request.user.id
        print(self.request.user.id)
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        pk = self.kwargs.get('pk')
        
        context = super(ProductoEdit, self).get_context_data(**kwargs)
        context["categorias"] = Categoria.objects.all()
        context["subcategorias"] = SubCategoria.objects.all()
        context["obj"] = Producto.objects.filter(pk=pk).first()
        
        return context

@login_required(login_url = '/login/')
@permission_required('inv.change_producto', login_url='bases:sin_privilegios')
def producto_inactivar(request, id):
    prod = Producto.objects.filter(pk=id).first()
    contexto={}
    template_name="inv/catalogos_del.html"

    if not prod:
        return redirect("inv:producto_list")
    
    if request.method=='GET':
        contexto={'obj':prod}

    if request.method=='POST':
        prod.estado=False
        prod.save()
        return redirect("inv:producto_list")
    
    return render(request,template_name,contexto)