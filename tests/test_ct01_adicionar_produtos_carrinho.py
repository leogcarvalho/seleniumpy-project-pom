import pytest
from pages.carrinho_page import CarrinhoPage
from pages.home_page import HomePage
from pages.login_page import LoginPage


@pytest.mark.usefixtures("setup_teardown")
@pytest.mark.carrinho
@pytest.mark.smoke
class TestCT01:
    def test_ct01_adicionar_produtos_carrinho(self):
        login_page = LoginPage()
        home_page = HomePage()
        carrinho_page = CarrinhoPage()

        produto_1 = "Sauce Labs Backpack"
        produto_2 = "Sauce Labs Bolt T-Shirt"

        # Fazendo login
        login_page.fazer_login("standard_user", "secret_sauce")

        # Adicionando a mochila ao carrinho
        home_page.adicionar_ao_carrinho(produto_1)

        # Verificando que a mochila foi adicionada
        home_page.acessar_carrinho()
        carrinho_page.verificar_produto_carrinho_existe(produto_1)

        # Clicando para voltar para a tela de produtos
        carrinho_page.clicar_continuar_comprando()

        # Adicionando mais um produto ao carrinho
        home_page.adicionar_ao_carrinho(produto_2)

        # Verificando que os 2 produtos estão no carrinho
        home_page.acessar_carrinho()
        carrinho_page.verificar_produto_carrinho_existe(produto_1)
        carrinho_page.verificar_produto_carrinho_existe(produto_2)
