from django.db import models
import core, inventory
# Create your models here.
from django.conf import settings



TYPE_CHOICES = (
    ('BC' ,'Bon de commande'),
    ('FF' ,'Facture finale'),
    ('BL' ,'Bon de livraison'),
)

SUPPLY_CHOICES = (
    ('BC' ,'Bon de commande'),
    ('BR' ,'Bon de récéption'),
)

################# DELIVERY  #################

class Wilaya(models.Model):
    name           = models.CharField(max_length=40, verbose_name="Wilaya", unique=True)
    relai_delivery = models.DecimalField( max_digits=8, verbose_name="Livraison point de Relais", decimal_places=2, default=0)
    home_delivery  = models.DecimalField( max_digits=10, verbose_name="Livraison à domicile", decimal_places=2, default=0)
    active         = models.BooleanField(default=True, verbose_name="Livraison Active")
    created        = models.DateTimeField(verbose_name='Date de Création', auto_now_add=True)
    updated        = models.DateTimeField(verbose_name='Date de dernière mise à jour', auto_now=True)
    class Meta:
        verbose_name = "Wilaya"
        verbose_name_plural = "1. Wilayas"

    def __str__(self):
        return self.name

class Commune(models.Model):
    wilaya = models.ForeignKey(Wilaya, on_delete=models.CASCADE, verbose_name="Wilaya")
    name = models.CharField(max_length=30, verbose_name="Commune")
    # active = models.BooleanField(default=True, verbose_name="Livraison Active")
    created      = models.DateTimeField(verbose_name='Date de Création', auto_now_add=True)
    updated      = models.DateTimeField(verbose_name='Date de dernière mise à jour', auto_now=True)
    class Meta:
        verbose_name = "Commune"
        verbose_name_plural = "2. Communes"        
    def __str__(self):
        return self.name
        

class WareHouseOrder(models.Model):
    sender = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name="sender", on_delete=models.CASCADE, related_name="set_orders")
    receiver = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name="receiver", on_delete=models.CASCADE, related_name="get_orders")
    delivery_man = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name="livreur", on_delete=models.CASCADE, related_name="internal_orders")
    order_type = models.CharField(choices=TYPE_CHOICES,verbose_name="type de commande", max_length=2, null=True, blank=True)
    is_confirmed = models.BooleanField(default=False)
    is_paid = models.BooleanField(default=False)
    is_delivered = models.BooleanField(default=False)
    is_return = models.BooleanField(default=False)
    discount = models.DecimalField(verbose_name="remise", max_digits=10, decimal_places=2, null=True, blank=True)
    delivery_cost =  models.DecimalField(verbose_name="cout de livraison", max_digits=10, decimal_places=2, null=True, blank=True)
    note  = models.TextField(null=True, blank=True)
    created      = models.DateTimeField(verbose_name='Date de Création', auto_now_add=True)
    updated      = models.DateTimeField(verbose_name='Date de dernière mise à jour', auto_now=True)
    class Meta:
        verbose_name ="WareHouseOrder"
        verbose_name_plural = "WareHouseOrders"

    def __str__(self): 
        return str(self.sender)

    def get_absolute_url(self):
        return reverse("order:warehouse_order_detail", kwargs={"pk": self.pk})

class WareHouseOrderItem(models.Model):
    order           = models.ForeignKey(WareHouseOrder, verbose_name="commande", on_delete=models.CASCADE, related_name="items")
    warehouse_item  = models.ForeignKey("inventory.WareHouseItem", verbose_name="produit", on_delete=models.CASCADE, related_name="warehouse_order_items")
    quantity        = models.IntegerField(verbose_name="quantité", default=1)
    price           = models.DecimalField(verbose_name="prix", max_digits=10, decimal_places=2, null=True, blank=True)
    created      = models.DateTimeField(verbose_name='Date de Création', auto_now_add=True)
    updated      = models.DateTimeField(verbose_name='Date de dernière mise à jour', auto_now=True)

    def get_price(self):
        return self.price * self.quantity

    def __str__(self):
        return str(self.warehouse_item)

    # def get_absolute_url(self):
    #     return reverse("order:warehouse_order_item_detail", kwargs={"pk": self.pk}) 


#################


class ClientOrder(models.Model):
    sender          = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name="sender", on_delete=models.CASCADE, related_name="set_client_orders")
    delivery_man = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name="livreur", on_delete=models.CASCADE, related_name="client_orders")
    first_name      = models.CharField(verbose_name="Nom" , max_length=50, null=True, blank=True)
    last_name       = models.CharField(verbose_name="Prenom" , max_length=50, null=True, blank=True)
    address         = models.CharField(verbose_name="Adresse" , max_length=250, null=True, blank=True)
    phone           = models.CharField(verbose_name="Téléphone" , max_length=25)
    email           = models.EmailField(verbose_name="E-mail", null=True, blank=True)
    commune         = models.ForeignKey(Commune, on_delete=models.SET_NULL, null=True, blank=True)
    order_type      = models.CharField(choices=TYPE_CHOICES,verbose_name="type de commande", max_length=2, null=True, blank=True)
    is_confirmed    = models.BooleanField(default=False)
    is_paid         = models.BooleanField(default=False)
    is_delivered    = models.BooleanField(default=False)
    is_cib          = models.BooleanField(default=False)
    cib_order_code  = models.CharField(verbose_name="code de commande cib", max_length=2, null=True, blank=True)
    coupon          = models.CharField(verbose_name="coupon", max_length=2, null=True, blank=True)
    is_return       = models.BooleanField(default=False)
    discount        = models.DecimalField(verbose_name="remise", max_digits=10, decimal_places=2, null=True, blank=True)
    delivery_cost   =  models.DecimalField(verbose_name="cout de livraison", max_digits=10, decimal_places=2, null=True, blank=True)
    note            = models.TextField(null=True, blank=True)
    created      = models.DateTimeField(verbose_name='Date de Création', auto_now_add=True)
    updated      = models.DateTimeField(verbose_name='Date de dernière mise à jour', auto_now=True)
    class Meta:
        verbose_name = "ClientOrder"
        verbose_name_plural = "ClientOrders"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("order:client_order_detail", kwargs={"pk": self.pk})

class ClientOrderItem(models.Model):
    order           = models.ForeignKey(ClientOrder, verbose_name="commande", on_delete=models.CASCADE, related_name="client_orders")
    warehouse_item  = models.ForeignKey("inventory.WareHouseItem", verbose_name="produit", on_delete=models.CASCADE, related_name="client_order_items")
    quantity        = models.IntegerField(verbose_name="quantité", default=1)
    price           = models.DecimalField(verbose_name="prix", max_digits=10, decimal_places=2, null=True, blank=True)
    created      = models.DateTimeField(verbose_name='Date de Création', auto_now_add=True)
    updated      = models.DateTimeField(verbose_name='Date de dernière mise à jour', auto_now=True)
    def get_absolute_url(self):
        return reverse("order:client_order_item_detail", kwargs={"pk": self.pk})


################# SUPPLY  #################

class Supplier(models.Model):
    Name    = models.CharField(verbose_name="Nom du fournisseur", max_length=150, null=True, blank=True)
    adress  = models.CharField(verbose_name="Adresse du fournisseur", max_length=150, null=True, blank=True)
    rc_code = models.CharField(verbose_name="numéro du registre de commerce", max_length=150, null=True, blank=True)
    art_code= models.CharField(verbose_name="numéro d'article", max_length=150, null=True, blank=True)
    nif_code= models.CharField(verbose_name="numéro identité fiscale", max_length=150, null=True, blank=True)
    created      = models.DateTimeField(verbose_name='Date de Création', auto_now_add=True)
    updated      = models.DateTimeField(verbose_name='Date de dernière mise à jour', auto_now=True)

    class Meta:
        verbose_name ="supplier"
        verbose_name_plural ="suppliers"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("order:supplier_detail", kwargs={"pk": self.pk})

class SupplyOrder(models.Model):
    supplier = models.ForeignKey(Supplier, verbose_name="sender", on_delete=models.CASCADE, related_name="sent_orders")
    receiver = models.ForeignKey("inventory.WareHouse", verbose_name="receiver", on_delete=models.CASCADE, related_name="supply_orders")
    supply_type = models.CharField(choices=SUPPLY_CHOICES,verbose_name="type de commande", max_length=2, null=True, blank=True)
    is_confirmed = models.BooleanField(default=False)
    is_paid = models.BooleanField(default=False)
    is_received = models.BooleanField(default=False)
    is_return = models.BooleanField(default=False)
    discount = models.DecimalField(verbose_name="remise", max_digits=10, decimal_places=2, null=True, blank=True)
    delivery_cost =  models.DecimalField(verbose_name="cout de livraison", max_digits=10, decimal_places=2, null=True, blank=True)
    note  = models.TextField(null=True, blank=True)
    created      = models.DateTimeField(verbose_name='Date de Création', auto_now_add=True)
    updated      = models.DateTimeField(verbose_name='Date de dernière mise à jour', auto_now=True)

    class Meta:
        verbose_name ="supply_order"
        verbose_name_plural ="supply_orders"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("order:supply_order_detail", kwargs={"pk": self.pk})

class SupplyOrderItem(models.Model):
    order           = models.ForeignKey(SupplyOrder, verbose_name="commande", on_delete=models.CASCADE, related_name="supply_order_items")
    warehouse_item  = models.ForeignKey("inventory.WareHouseItem", verbose_name="produit", on_delete=models.CASCADE)
    quantity        = models.IntegerField(verbose_name="quantité", default=1)
    is_received = models.BooleanField(default=False)
    price           = models.DecimalField(verbose_name="prix", max_digits=10, decimal_places=2, null=True, blank=True)
    note  = models.TextField(null=True, blank=True)
    created      = models.DateTimeField(verbose_name='Date de Création', auto_now_add=True)
    updated      = models.DateTimeField(verbose_name='Date de dernière mise à jour', auto_now=True)
    def get_absolute_url(self):
        return reverse("order:client_order_item_detail", kwargs={"pk": self.pk})


