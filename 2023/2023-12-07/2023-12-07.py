class AdventOfCode:
    def __init__(self, filename):
        with open(filename, 'r') as f:
            self.lines_list = f.read().splitlines()

        self.hand_bid_dict = {}
        self.hands_list = []
        self.bids_list = []
        for line in self.lines_list:
            hand, bid = line.split(' ')
            self.hand_bid_dict[hand] = int(bid)
            self.hands_list.append(hand)
            self.bids_list.append(bid)

        self.strength_dict_puzzle_1 = {}
        self.strength_dict_puzzle_2 = {}
        self.rank_hand_dict = {}

        self.sum_of_puzzle_1 = 0
        self.sum_of_puzzle_2 = 0

    @staticmethod
    def get_strength_puzzle_1(hand):
        card_1 = hand[0]
        card_2 = hand[1]
        card_3 = hand[2]
        card_4 = hand[3]
        card_5 = hand[4]
        card_list = [card_1, card_2, card_3, card_4, card_5]
        sorted_card_list = sorted(card_list)
        sorted_card_1 = sorted_card_list[0]
        sorted_card_2 = sorted_card_list[1]
        sorted_card_3 = sorted_card_list[2]
        sorted_card_4 = sorted_card_list[3]
        sorted_card_5 = sorted_card_list[4]

        # Five of a kind, where all five cards have the same label: AAAAA
        if card_1 == card_2 == card_3 == card_4 == card_5:
            return 1  # 'five_of_a_kind'
        # Four of a kind, where four cards have the same label and one card has a different label: AA8AA
        if ((sorted_card_1 == sorted_card_2 == sorted_card_3 == sorted_card_4) or
                (sorted_card_2 == sorted_card_3 == sorted_card_4 == sorted_card_5)):
            return 2  # 'four_of_a_kind'
        # Full house, where three cards have the same label, and the remaining two cards share a different label: 23332
        if (((sorted_card_1 == sorted_card_2 == sorted_card_3) and (sorted_card_4 == sorted_card_5)) or
                ((sorted_card_1 == sorted_card_2) and (sorted_card_3 == sorted_card_4 == sorted_card_5))):
            return 3  # 'full_house'
        # Three of a kind, where three cards have the same label, and the remaining two cards are each different from
        # any other card in the hand: TTT98
        if ((sorted_card_1 == sorted_card_2 == sorted_card_3) or
                (sorted_card_2 == sorted_card_3 == sorted_card_4) or
                (sorted_card_3 == sorted_card_4 == sorted_card_5)):
            return 4  # 'three_of_a_kind'
        # Two pair, where two cards share one label, two other cards share a second label, and the remaining card has a
        # third label: 23432
        if (((sorted_card_1 == sorted_card_2) and (sorted_card_3 == sorted_card_4)) or
                ((sorted_card_1 == sorted_card_2) and (sorted_card_4 == sorted_card_5)) or
                ((sorted_card_2 == sorted_card_3) and (sorted_card_4 == sorted_card_5))):
            return 5  # 'two_pair'
        # One pair, where two cards share one label, and the other three cards have a different label from the pair and
        # each other: A23A4
        if ((sorted_card_1 == sorted_card_2) or
                (sorted_card_2 == sorted_card_3) or
                (sorted_card_3 == sorted_card_4) or
                (sorted_card_4 == sorted_card_5)):
            return 6  # 'one_pair'
        # High card where all cards' labels are distinct: 23456
        return 7

    def get_non_joker_hand(self, hand):
        card_occurrences_dict = {}
        for card in hand:
            if card != 'J':
                if card in card_occurrences_dict:
                    card_occurrences_dict[card] += 1
                else:
                    card_occurrences_dict[card] = 1

        try:
            max_occurrences = max(card_occurrences_dict.values())
        except:
            max_occurrences = 5

        for card in ['A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3', '2']:
            if card in card_occurrences_dict:
                if card_occurrences_dict[card] == max_occurrences:
                    hand = hand.replace('J', card)

        return hand

    def get_strength_puzzle_2(self, hand):
        non_joker_hand = self.get_non_joker_hand(hand)

        card_1 = non_joker_hand[0]
        card_2 = non_joker_hand[1]
        card_3 = non_joker_hand[2]
        card_4 = non_joker_hand[3]
        card_5 = non_joker_hand[4]
        card_list = [card_1, card_2, card_3, card_4, card_5]
        sorted_card_list = sorted(card_list)
        sorted_card_1 = sorted_card_list[0]
        sorted_card_2 = sorted_card_list[1]
        sorted_card_3 = sorted_card_list[2]
        sorted_card_4 = sorted_card_list[3]
        sorted_card_5 = sorted_card_list[4]

        # Five of a kind, where all five cards have the same label: AAAAA
        if card_1 == card_2 == card_3 == card_4 == card_5:
            return 1  # 'five_of_a_kind'
        # Four of a kind, where four cards have the same label and one card has a different label: AA8AA
        if ((sorted_card_1 == sorted_card_2 == sorted_card_3 == sorted_card_4) or
                (sorted_card_2 == sorted_card_3 == sorted_card_4 == sorted_card_5)):
            return 2  # 'four_of_a_kind'
        # Full house, where three cards have the same label, and the remaining two cards share a different label: 23332
        if (((sorted_card_1 == sorted_card_2 == sorted_card_3) and (sorted_card_4 == sorted_card_5)) or
                ((sorted_card_1 == sorted_card_2) and (sorted_card_3 == sorted_card_4 == sorted_card_5))):
            return 3  # 'full_house'
        # Three of a kind, where three cards have the same label, and the remaining two cards are each different from
        # any other card in the hand: TTT98
        if ((sorted_card_1 == sorted_card_2 == sorted_card_3) or
                (sorted_card_2 == sorted_card_3 == sorted_card_4) or
                (sorted_card_3 == sorted_card_4 == sorted_card_5)):
            return 4  # 'three_of_a_kind'
        # Two pair, where two cards share one label, two other cards share a second label, and the remaining card has a
        # third label: 23432
        if (((sorted_card_1 == sorted_card_2) and (sorted_card_3 == sorted_card_4)) or
                ((sorted_card_1 == sorted_card_2) and (sorted_card_4 == sorted_card_5)) or
                ((sorted_card_2 == sorted_card_3) and (sorted_card_4 == sorted_card_5))):
            return 5  # 'two_pair'
        # One pair, where two cards share one label, and the other three cards have a different label from the pair and
        # each other: A23A4
        if ((sorted_card_1 == sorted_card_2) or
                (sorted_card_2 == sorted_card_3) or
                (sorted_card_3 == sorted_card_4) or
                (sorted_card_4 == sorted_card_5)):
            return 6  # 'one_pair'
        # High card where all cards' labels are distinct: 23456
        return 7

    @staticmethod
    def get_translated_hand_puzzle_1(hand):
        translated_hand = ''
        translation_dict = {
            'A': 'A',
            'K': 'B',
            'Q': 'C',
            'J': 'D',
            'T': 'E',
            '9': 'F',
            '8': 'G',
            '7': 'H',
            '6': 'I',
            '5': 'J',
            '4': 'K',
            '3': 'L',
            '2': 'M'
        }

        for card in hand:
            translated_hand += translation_dict[card]

        return translated_hand

    @staticmethod
    def get_translated_hand_puzzle_2(hand):
        translated_hand = ''
        translation_dict = {
            'A': 'A',
            'K': 'B',
            'Q': 'C',
            'T': 'D',
            '9': 'E',
            '8': 'F',
            '7': 'G',
            '6': 'H',
            '5': 'I',
            '4': 'J',
            '3': 'K',
            '2': 'L',
            'J': 'M'
        }

        for card in hand:
            translated_hand += translation_dict[card]

        return translated_hand

    @staticmethod
    def get_untranslated_hand_puzzle_1(translated_hand):
        untranslated_hand = ''
        translation_dict = {
            'A': 'A',
            'B': 'K',
            'C': 'Q',
            'D': 'J',
            'E': 'T',
            'F': '9',
            'G': '8',
            'H': '7',
            'I': '6',
            'J': '5',
            'K': '4',
            'L': '3',
            'M': '2'
        }

        for card in translated_hand:
            untranslated_hand += translation_dict[card]

        return untranslated_hand

    @staticmethod
    def get_untranslated_hand_puzzle_2(translated_hand):
        untranslated_hand = ''
        translation_dict = {
            'A': 'A',
            'B': 'K',
            'C': 'Q',
            'D': 'T',
            'E': '9',
            'F': '8',
            'G': '7',
            'H': '6',
            'I': '5',
            'J': '4',
            'K': '3',
            'L': '2',
            'M': 'J'
        }

        for card in translated_hand:
            untranslated_hand += translation_dict[card]

        return untranslated_hand

    def get_ordered_hands_list_puzzle_1(self, hands_list):
        translated_hands_list = []
        for hand in hands_list:
            translated_hands_list.append(self.get_translated_hand_puzzle_1(hand))

        translated_hands_list = sorted(translated_hands_list)

        sorted_untranslated_hands_list = []
        for translated_hand in translated_hands_list:
            sorted_untranslated_hands_list.append(self.get_untranslated_hand_puzzle_1(translated_hand))

        return sorted_untranslated_hands_list

    def get_ordered_hands_list_puzzle_2(self, hands_list):
        translated_hands_list = []
        for hand in hands_list:
            translated_hands_list.append(self.get_translated_hand_puzzle_2(hand))

        translated_hands_list = sorted(translated_hands_list)

        sorted_untranslated_hands_list = []
        for translated_hand in translated_hands_list:
            sorted_untranslated_hands_list.append(self.get_untranslated_hand_puzzle_2(translated_hand))

        return sorted_untranslated_hands_list

    def solve_part_1(self):
        for index, hand in enumerate(self.hands_list):
            strength = self.get_strength_puzzle_1(hand)
            if strength in self.strength_dict_puzzle_1:
                self.strength_dict_puzzle_1[strength].append(hand)
            else:
                self.strength_dict_puzzle_1[strength] = [hand]

        rank = len(self.hands_list)
        for strength in sorted(self.strength_dict_puzzle_1.keys()):
            ordered_hands_list = self.get_ordered_hands_list_puzzle_1(self.strength_dict_puzzle_1[strength])

            for sorted_hand in ordered_hands_list:
                self.rank_hand_dict[rank] = sorted_hand
                bid = self.hand_bid_dict[sorted_hand]
                total_winnings = bid * rank
                self.sum_of_puzzle_1 += total_winnings
                rank -= 1

        return f'\nResult puzzle 1: {self.sum_of_puzzle_1}\n'

    def solve_part_2(self):
        for index, hand in enumerate(self.hands_list):
            strength = self.get_strength_puzzle_2(hand)
            if strength in self.strength_dict_puzzle_2:
                self.strength_dict_puzzle_2[strength].append(hand)
            else:
                self.strength_dict_puzzle_2[strength] = [hand]

        print(self.strength_dict_puzzle_2)

        strength_ordered_hands_dict = {}
        rank = len(self.hands_list)
        for strength in sorted(self.strength_dict_puzzle_2.keys()):
            ordered_hands_list = self.get_ordered_hands_list_puzzle_2(self.strength_dict_puzzle_2[strength])

            strength_ordered_hands_dict[strength] = ordered_hands_list

            for sorted_hand in ordered_hands_list:
                self.rank_hand_dict[rank] = sorted_hand
                bid = self.hand_bid_dict[sorted_hand]
                total_winnings = bid * rank
                self.sum_of_puzzle_2 += total_winnings
                rank -= 1

        print(strength_ordered_hands_dict)

        return f'\nResult puzzle 2: {self.sum_of_puzzle_2}'


puzzle = AdventOfCode('input.txt')
print(puzzle.solve_part_1())
print(puzzle.solve_part_2())
