# Elementos consulta fipe
consulta_carro = {
    'expandir_campos': "//li[@class='ilustra']//a[@data-slug='carro']",
    'pesquisa_comum': "//a[contains(text(), 'Pesquisa comum') and @data-slug='carro-comum']",
    'span_marca': "//div[@id='selectMarcacarro_chosen']",
    'input_marca': "//div[@id='selectMarcacarro_chosen']//input[@type='text']",
    'span_modelo': "//div[@id='selectAnoModelocarro_chosen']",
    'input_modelo': "//div[@id='selectAnoModelocarro_chosen']//input[@type='text']",
    'lista_modelos': "//div[@id='selectAnoModelocarro_chosen']//div[@class='chosen-drop']//ul[@class='chosen-results']//li[contains(@class, 'active-result')]",
    'span_ano': "//div[@id='selectAnocarro_chosen']",
    'input_ano': "//div[@id='selectAnocarro_chosen']//input[@type='text']",
    'lista_ano': "//div[@id='selectAnocarro_chosen']//div[@class='chosen-drop']//ul[@class='chosen-results']//li[contains(@class, 'active-result')]",
    'button_pesquisar': "//a[@id='buttonPesquisarcarro' and contains(text(), 'Pesquisar')]",
    'button_limpar_pesquisa': "//div[@id='buttonLimparPesquisarcarro']"
}
# Elementos do resultado
elemento_pesquisa = "(//div[@data-tipo='resultadoConsulta']//p)["
resultado_pesquisa = {
    'fipe': elemento_pesquisa + "4]",
    'marca': elemento_pesquisa + "6]",
    'modelo': elemento_pesquisa + "8]",
    'ano': elemento_pesquisa + "10]",
    'valor': elemento_pesquisa + "16]"
}