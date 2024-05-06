import os
from PIL import Image

def convert_image(input_path, output_path, base_name):
    files = os.listdir(input_path)
    counter = 1
    
    for file in files:
        input_file_path = os.path.join(input_path, file)
        
        if os.path.isfile(input_file_path) and any(input_file_path.endswith(ext) for ext in ['.jpg', '.png', '.jpeg']):
            image = Image.open(input_file_path)
            
            width, height = image.size
            
            # Calcula o fator de escala necessário para preencher a imagem no quadrado de 1000x1000
            scale_factor = max(1000/width, 1000/height)
            
            # Calcula o novo tamanho da imagem
            new_width = int(width * scale_factor)
            new_height = int(height * scale_factor)
            
            # Redimensiona a imagem
            new_image = image.resize((new_width, new_height))
            
            # Cria uma nova imagem sem fundo
            new_square_image = Image.new("RGBA", (1000, 1000))
            
            # Cola a imagem redimensionada no canto superior esquerdo da nova imagem
            new_square_image.paste(new_image, ((1000 - new_width) // 2, (1000 - new_height) // 2))
            
            # Salva a imagem com o nome adequado
            output_file_name = f'{base_name}_{counter:02}.png'
            output_file_path = os.path.join(output_path, output_file_name)
            new_square_image.save(output_file_path)
            
            print(f'Imagem convertida e salva como {output_file_path}')
            
            counter += 1

def get_base_name():
    return input("Digite o nome base para os arquivos convertidos: ")

def main():
    input_path = 'input'
    output_path = 'output'
    
    if not os.path.exists(output_path):
        os.makedirs(output_path)
    
    base_name = get_base_name()
    convert_image(input_path, output_path, base_name)

if __name__ == "__main__":
    main()
