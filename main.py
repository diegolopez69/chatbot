import re
import random


def get_response(user_input):
    split_message = re.split(r'\s|[,:;.?!-_]\s*', user_input.lower())
    response = check_all_messages(split_message)
    return response


def message_probability(user_message, recognized_words, single_response=False, required_word=[]):
    message_certainty = 0
    has_required_words = True

    for word in user_message:
        if word in recognized_words:
            message_certainty += 1

    percentage = float(message_certainty) / float(len(recognized_words))

    for word in required_word:
        if word not in user_message:
            has_required_words = False
            break
    if has_required_words or single_response:
        return int(percentage * 100)
    else:
        return 0


def check_all_messages(message):
    highest_prob = {}

    def response(bot_response, list_of_words, single_response=False, required_words=[]):
        nonlocal highest_prob
        highest_prob[bot_response] = message_probability(
            message, list_of_words, single_response, required_words)

    response('Hola soy Odin, el chatbot que resolverá tus problemas', [
             'hola', 'saludos', 'buenas', 'buenos dias', 'buenas tardes', 'buenas tardes', ], single_response=True)
    response('Presiona la tecla "Windows" + "P" y selecciona la opción de duplicado',
             ['No', 'funciona', 'proyecto', 'no va', 'va', 'sirve', 'puedo'], required_words=['proyector'])

    # response('Verifica que el ordenador este en la red wifi correcta', [
    #     'entrar a mi usuario', 'puedo', 'entrar', 'a mi', 'usuario'], required_words=['usuario'])

    # response('Verifica que el ordenador este en la red wifi correcta', [
    #     'entrar a mi usuario', 'puedo', 'entrar', 'a mi', 'usuario'], single_response=True)

    response('Verifica que el ordenador este en la red wifi correcta', [
             'No', 'puedo', 'sirve', 'funciona', 'acceder', 'entrar', 'iniciar', 'a mi', 'usuario'], required_words=['usuario'])

    response('Verifica que el ordenador este en la red wifi correcta', [
             'No', 'puedo', 'sirve', 'funciona', 'acceder', 'entrar', 'iniciar', 'a mi', 'perfil'], required_words=['perfil'])

    response('Verifica que el cable de internet este conectado al ordenador', [
        'No hay wifi', 'wifi'], single_response=True)

    response('Puedes ser más específico en que es lo que ya hiciste, por favor', [
             'Ya lo hice', 'Lo acabo de hacer', 'ya'], single_response=True)

    response('Cuentame con que necesitas ayuda', [
        'ayuda', 'necesito ayuda', 'necesito'], single_response=True)

    response('La extensión para resolver problemas es 1972', [
        'Cual es la', 'extensión', 'extension'], single_response=True)

    response('Siempre a la orden', [
             'gracias', 'te lo agradezco', 'thanks', 'adios'], single_response=True)

    best_match = max(highest_prob, key=highest_prob.get)
    # print(highest_prob)

    return unknown() if highest_prob[best_match] < 1 else best_match


def unknown():
    response = [
        'Lo siento no comprendo tu pregunta, prueba escribiendola de otra manera'][random.randrange(1)]
    return response


while True:
    print("Odin: " + get_response(input('Tú: ')))
