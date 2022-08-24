from treys import Card, Evaluator
board = [Card.new('6h'),Card.new('7h'),Card.new('8h')]
hand = [Card.new('As'),Card.new('Jc')]

evaluator = Evaluator()
print (evaluator.evaluate(board, hand))