
from django.db import models
import qrcode
from io import BytesIO
from django.core.files import File

#Funcionarios    
class Cooperado(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nome')
    mat= models.IntegerField( verbose_name= 'Matricula')
    cpf = models.IntegerField( verbose_name= 'CPF')
    rg = models.IntegerField(  verbose_name='RG')
    is_active = models.BooleanField(default=True, verbose_name='Ativo')
    is_inactive = models.BooleanField(default=False,verbose_name='Inativo')
    description = models.TextField(null=True, blank=True, verbose_name='Descrição')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Criado em')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Atualizado em')
    
    class Meta:
        ordering = ['name']
        verbose_name = 'Funcionario'

    def __str__(self):
        return self.name
    
#Prestadores de serviço    
class Prestador(models.Model):
    title = models.CharField(max_length=100, verbose_name='Nome')
    mat= models.CharField(max_length=20,verbose_name= 'CNPJ')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Preço')
    is_active = models.BooleanField(default=True, verbose_name='Ativo')
    is_inactive = models.BooleanField(verbose_name='Inativo')
    description = models.TextField(null=True, blank=True, verbose_name='Descrição')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Criado em')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Atualizado em')
    
    class Meta:
        ordering = ['title']
        verbose_name = 'Prestador'

    def __str__(self):
        return self.title

#Marca
class Brand(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nome')
    #is_active = models.BooleanField(default=True, verbose_name='Ativo')
    description = models.TextField(null=True, blank=True, verbose_name='Descrição')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Criado em')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Atualizado em')

    class Meta:
        ordering = ['name']
        verbose_name = 'Marca'

    def __str__(self):
        return self.name

#Departamento
class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nome')
    is_active = models.BooleanField(default=True, verbose_name='Ativo')
    description = models.TextField(null=True, blank=True, verbose_name='Descrição')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Criado em')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Atualizado em')

    class Meta:
        ordering = ['name']
        verbose_name = 'Departamento'

    def __str__(self):
        return self.name

# Maquinas
class Product(models.Model):
    #name= models.ForeignKey(Cooperado, on_delete= models.PROTECT,related_name='products', verbose_name='Nome')
    title = models.CharField(max_length=100, verbose_name='Título')
    brand = models.ForeignKey(Brand, on_delete=models.PROTECT,
                              related_name='products', verbose_name='Marca')
    patrimonio = models.ForeignKey(Prestador, on_delete=models.PROTECT,
                              related_name='products', default=0, verbose_name='Prestador')
    processor = models.CharField(max_length=10, verbose_name='Processador')
    memory_ram = models.CharField(max_length=10, verbose_name='Memoria Ram')
    storage = models.CharField(max_length=10, verbose_name='Armazenamento')
    category = models.ForeignKey(Category, on_delete=models.PROTECT,
                                 related_name='products', verbose_name='Departamento')
    price = models.DecimalField(max_digits=10, decimal_places=2,default= 0, verbose_name='Preço')
    is_active = models.BooleanField(default=True, verbose_name='Ativo')
    description = models.TextField(null=True, blank=True, verbose_name='Descrição')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Criado em')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Atualizado em')
    qr_code = models.ImageField(upload_to='qr_codes/', blank=True, null=True)

    def save(self, *args, **kwargs):
        # 1. Garante que o ID existe (salva primeiro se for novo)
        if not self.id:
            super().save(*args, **kwargs)

        # 2. Define o conteúdo fixo do QR Code
        # Substitua pelo seu domínio real ou IP do servidor
        url_do_produto = f"192.168.15.20:8000/{self.id}/"

        # 3. Configura e gera o QR Code
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(url_do_produto)
        qr.make(fit=True)

        # Cria a imagem a partir do objeto QR
        img = qr.make_image(fill_color="black", back_color="white")
        
        # 4. Salva a imagem no campo ImageField sem causar loop infinito
        buffer = BytesIO()
        img.save(buffer, format='PNG')
        fname = f'qr_code-{self.id}.png'
        
        # O 'save=False' no self.qr_code.save evita que o save() do model 
        # seja chamado novamente em loop
        self.qr_code.save(fname, File(buffer), save=False)
        
        # Salva o campo qr_code no banco
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.title
#Perifericos
class Perifericos(models.Model):
    title = models.CharField(max_length=100,verbose_name='Titulo')
    modelo = models.CharField(max_length=100,verbose_name='Modelo')
    amount = models.CharField(max_length=100,verbose_name='Quantidade')
    brand = models.ForeignKey(Brand, on_delete= models.PROTECT,
                              related_name='produtos', verbose_name='Marca')
    is_new = models.BooleanField(default=True, verbose_name= 'Novo')
    is_used = models.BooleanField(default=True, verbose_name= 'Usado')
    delivery = models.DateTimeField(auto_now_add=True, verbose_name='Entregue em')
    description = models.TextField(null=True, blank=True, verbose_name='Descrição')
    
    class Meta:
        ordering = ['title']
        verbose_name = 'Periferico'

    def __str__(self):
        return self.title
    
#Filiais
class Branch(models.Model):
    name = models.TextField(null=True, blank=True, verbose_name='Nome')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Criado em')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Atualizado em')

    class Meta:
        ordering = ['name']
        verbose_name = 'Filial'

    def __str__(self):
        return self.name
    
#Celulares
class Phone (models.Model):
    title = models.CharField(max_length=100, verbose_name='Nome')
    brand = models.ForeignKey(Brand, on_delete=models.PROTECT,
                              related_name='phon', verbose_name='Marca')
    storage = models.CharField(max_length=10, verbose_name='Armazenamento')
    number = models.IntegerField(default="0",verbose_name='Telefone')
    imei= models.CharField(max_length=30,verbose_name='IMEI')
    category = models.ForeignKey(Category, on_delete=models.PROTECT,
                                 related_name='phone', verbose_name='Departamento')
    is_termo_active = models.BooleanField(default=True, verbose_name= 'Assinado')
    is_termo_inactive = models.BooleanField(default=False, verbose_name= 'Não assinou')
    is_active = models.BooleanField(default=True, verbose_name='Ativo')
    last_user = models.ForeignKey(Cooperado,on_delete=models.PROTECT,
                                 related_name='phone', verbose_name='Ultimo Usuario')
    description = models.TextField(null=True, blank=True, verbose_name='Descrição')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Criado em')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Atualizado em')

    class Meta:
        ordering = ['title']
        verbose_name = 'Celulare'

    def __str__(self):
        return self.title

#Controle do notebooks,celulares pelo nome do usuario
class Controle(models.Model):
    name= models.ForeignKey(Cooperado, on_delete= models.PROTECT,
                            related_name='controls', verbose_name='Nome')
    branch = models.ForeignKey(Branch, on_delete= models.PROTECT, 
                            related_name='controls', verbose_name='Filial')
    phones = models.ForeignKey(Phone,on_delete= models.PROTECT,
                            related_name='controls', verbose_name='Celular' )
    laptop = models.ForeignKey(Product, on_delete=models.PROTECT,
                               related_name='controls',verbose_name='Notebook')

    delivery = models.DateTimeField(auto_now_add=True, verbose_name='Entregue em')

    category = models.ForeignKey(Category, on_delete=models.PROTECT,
                                 related_name='controls', verbose_name='Departamento')
    
    img = models.ImageField(upload_to='products/',verbose_name='Imagem 1')
    img1 = models.ImageField(upload_to='products/',blank=True, null=True, verbose_name='Imagem 2')
    # img2 = models.ImageField(upload_to='products/',blank=True, null=True,verbose_name='Imagem 3')

    is_active = models.BooleanField(default=True, verbose_name='Ativo')
    is_inactive = models.BooleanField(default=False,verbose_name='Inativo')
    description = models.TextField(null=True, blank=True, verbose_name='Descrição')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Criado em')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Atualizado em')
    qr_code = models.ImageField(upload_to='qr_code/', blank=True, null=True)

    class Meta:
        ordering = ['name']
        verbose_name = 'Controle'

    def __str__(self):
        return str(self.name)
    
    def save(self, *args, **kwargs):
        # 1. Primeiro passo: Salva os dados básicos para garantir que o objeto tem um ID
        # Se não tiver ID, o super().save() cria um.
        is_new = self._state.adding
        super().save(*args, **kwargs)

        # 2. Se for um registro novo ou se o QR Code estiver vazio
        if is_new or not self.qr_code:
            # Importações internas para evitar erros no migrate
            # Conteúdo do QR Code (Sempre use a URL completa se possível)
            # Exemplo: https://caio12faculdade.pythonanywhere.com/controle/1/
            link_fixo = f"https://caio12faculdade.pythonanywhere.com/controle/{self.id}/"

            qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_L,
                box_size=10,
                border=4,
            )
            qr.add_data(link_fixo)
            qr.make(fit=True)

            img_qr = qr.make_image(fill_color="black", back_color="white")
            
            buffer = BytesIO()
            img_qr.save(buffer, format='PNG')
            
            # Define o nome do arquivo
            filename = f'qr_code_{self.id}.png'
            
            # Salva o arquivo no campo ImageField
            # save=False evita que entre em loop infinito chamando este save() de novo
            self.qr_code.save(filename, File(buffer), save=False)
            
            # Atualiza apenas a coluna do QR Code no banco de dados
            Controle.objects.filter(id=self.id).update(qr_code=self.qr_code)
    
    # def __str__(self):
    #     return self.name