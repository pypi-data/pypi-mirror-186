__all__ = [
    "RegexToolkit",
]

from collections.abc import Sequence, Iterable

# from regex_toolkit import emojis
# from regex_toolkit import confusables

import string



# class Characters:
#     digits: tuple[str, ...] = tuple(string.digits)
#     alpha: tuple[str, ...] = tuple(string.ascii_letters)
#     alphaspace: tuple[str, ...] = tuple(string.ascii_letters + " ")
#     alphanum: tuple[str, ...] = tuple(string.ascii_letters + string.digits)
#     at_signs: tuple[str, ...] = ("@", "\uff20")
#     pound_signs: tuple[str, ...] = ("#", "\uff03")
#     dollar_signs: tuple[str, ...] = ("$", "\uff04")
#     spaces: tuple[str, ...] = (
#         # SPACE
#         "\u0020",
#         # OGHAM SPACE MARK
#         "\u1680",
#         # MONGOLIAN VOWEL SEPARATOR
#         "\u180E",
#         # NO-BREAK SPACE
#         "\u00A0",
#         # MEDIUM MATHEMATICAL SPACE
#         "\u205F",
#         "\u2060",
#         "\u3000",
#     )
#     # Emojis
#     # emojis: tuple[str, ...] = emojis
#     # Confusables
#     # confusables: dict[str, tuple[str, ...]] = parse_confusables()
# 
#     # def __repr__(self) -> str:
#     #     return "<Characters>"
#     #
#     # def __str__(self) -> str:
#     #     return "Characters"
# 
# 
# class Expressions:
#     _lmda_escape = lambda x: f"\\{x}"
# 
#     # digits: str = r"[^\D]"
#     # alpha: str = r"[a-zA-Z]"
#     # alphaspace: str = r"[a-zA-Z ]"
#     # alphanum: str = r"[" + r"[0-9a-zA-Z]"
# 
#     # emojis: str = r"|".join(map(_lmda_escape, Characters.emojis))
# 
#     at_signs: str = r"|".join(map(_lmda_escape, Characters.at_signs))
#     pound_signs: str = r"|".join(map(_lmda_escape, Characters.pound_signs))
#     dollar_signs: str = r"|".join(map(_lmda_escape, Characters.dollar_signs))
#     spaces: str = r"|".join(map(_lmda_escape, Characters.spaces))


class RegexToolkit:
    _alpha_chars: set[str] = set(string.ascii_letters)
    _digit_chars: set[str] = set(string.digits)

    _safe_chars: set[str] = _alpha_chars.union(_digit_chars).union(set(string.whitespace))
    _escapable_chars: set[str] = set(string.punctuation)
    
    # Link Reference to Singleton
    # characters: Characters = Characters()
    # expressions: Expressions = Expressions()

    @staticmethod
    def iter_sort_by_len(texts: Iterable[str], reverse: bool = True) -> Iterable[str]:
        for text in sorted(texts, key=len, reverse=reverse):
            yield text

    @staticmethod
    def sort_by_len(texts: Iterable[str], reverse: bool = True) -> tuple[str, ...]:
        return tuple(RegexToolkit.iter_sort_by_len(texts, reverse=reverse))

    @staticmethod
    def ord_to_codepoint(ordinal: int) -> str:
        codepoint = format(ordinal, "x").zfill(8)
        return codepoint

    @staticmethod
    def char_to_codepoint(char: str) -> str:
        ordinal = ord(char)
        codepoint = RegexToolkit.ord_to_codepoint(ordinal)
        return codepoint

    @staticmethod
    def char_as_exp(char: str) -> str:
        """Create a re Regex Expression that Exactly Matches a Character

        Expressions like \s, \S, \d, \D, \1, etc. are reserved.

        Args:
            char (str): Character to match.

        Returns:
            str: re expression that exactly matches the original character.
        """
        # a-zA-Z0-9 characters already match the expression
        if char in RegexToolkit._safe_chars:
            return char

        # Uncommon characters are escaped using backslash
        return f"\\{char}"

    @staticmethod
    def char_as_exp2(char: str) -> str:
        """Create a re2 Regex Expression that Exactly Matches a Character

        Args:
            char (str): Character to match.

        Returns:
            str: re2 expression that exactly matches the original character.
        """
        # a-zA-Z0-9 characters already match the expression
        if char in RegexToolkit._safe_chars:
            return char

        # Common punctuation is safe to escape
        # - Escaping with backslash where possible reduces the size of the final expression.
        if char in RegexToolkit._escapable_chars:
            return f"\\{char}"

        # Uncommon characters are escaped using their codepoint
        return "\\x{" + RegexToolkit.char_to_codepoint(char) + "}"

    @staticmethod
    def string_as_exp(text: str) -> str:
        """Create a re Regex Expression that Exactly Matches a String

        Args:
            text (str): String to match.

        Returns:
            str: re expression that exactly matches the original string.
        """
        return r"".join(map(RegexToolkit.char_as_exp, text))

    @staticmethod
    def string_as_exp2(text: str) -> str:
        """Create a re2 Regex Expression that Exactly Matches a String

        Args:
            text (str): String to match.

        Returns:
            str: re2 expression that exactly matches the original string.
        """
        return r"".join(map(RegexToolkit.char_as_exp2, text))

    @staticmethod
    def strings_as_exp(texts: Iterable[str]) -> str:
        """re"""
        return r"|".join(
            map(
                RegexToolkit.string_as_exp,
                RegexToolkit.iter_sort_by_len(texts, reverse=True),
            )
        )

    @staticmethod
    def strings_as_exp2(texts: Iterable[str]) -> str:
        """re2"""
        return r"|".join(
            map(
                RegexToolkit.string_as_exp2,
                RegexToolkit.iter_sort_by_len(texts, reverse=True),
            )
        )

    @staticmethod
    def iter_char_range(first_codepoint: int, last_codepoint: int) -> Iterable[str]:
        """Iterate All Characters within a Range of Codepoints (Inclusive)

        Args:
            first_codepoint (int): Starting codepoint.
            last_codepoint (int): Final codepoint.

        Yields:
            str: Character from within a range of codepoints.
        """
        for i in range(ord(first_codepoint), ord(last_codepoint) + 1):
            yield chr(i)

    @staticmethod
    def char_range(first_codepoint: int, last_codepoint: int) -> tuple[str, ...]:
        """Tuple of All Characters within a Range of Codepoints (Inclusive)

        Args:
            first_codepoint (int): Starting codepoint.
            last_codepoint (int): Final codepoint.

        Returns:
            tuple[str, ...]: Characters within a range of codepoints.
        """
        return tuple(RegexToolkit.iter_char_range(first_codepoint, last_codepoint))

    @staticmethod
    def is_alphaspace(char: str) -> bool:
        return char in Characters.alphaspace

    @staticmethod
    def is_digit(char: str) -> bool:
        """Check if a Character is a Digit [0-9]

        Args:
            char (str): Character to check.

        Returns:
            bool: True if the character is a digit.
        """
        return char in Characters.digits

    @staticmethod
    def is_alpha(char: str) -> bool:
        return char in Characters.alpha

    @staticmethod
    def is_alphanum(char: str) -> bool:
        return char in Characters.alphanum

    @staticmethod
    def is_emoji(emoji: str) -> bool:
        return emoji in Characters.emojis

    @staticmethod
    def mask_span(text: str, span, mask: str | None = None) -> str:
        """Slice and Mask Text using a Span"""
        if mask is None:
            mask = ""

        return text[: span[0]] + mask + text[span[1] :]

    @staticmethod
    def mask_spans(
        text: str,
        spans: Iterable[Sequence[int]],
        masks: Iterable[str],
    ) -> str:
        """Slice and Mask a String using Multiple Spans

        NOTE: Original values for spans and masks parameters will be modified!

        Args:
            text (str): Text to slice.
            spans (Spans): Domains of index positions to mask from the text.
            masks (Masks, optional): Masks to insert when slicing. Defaults to None.

        Returns:
            str: Text with all spans replaced with the mask text.
        """
        for span, mask in reversed(zip(spans, masks)):
            text = RegexToolkit.mask_span(text, span, mask=mask)

        return text

    @staticmethod
    def to_utf8(text: str) -> str:
        """Force UTF-8 Text Encoding

        Args:
            text (str): Text to encode.

        Returns:
            str: Encoded text.
        """
        return text.encode("utf-8").decode("utf-8")

    # def normalize_spaces(text: str) -> str:
    #     pass


# class PartialExpressions:
#     pass
#
#
# class Expressions(PartialExpressions):
#     utf_chars: str = r"a-zA-Z0-9\u00c0-\u00d6\u00d8-\u00f6\u00f8-\u00ff"
#     at_signs: str = r"\@\uff20"
#     pound_signs: str = r"\#\uff03"
#     dollar_signs: str = r"\$\uff04"
#     spaces: str = r"\u0020\u00A0\u1680\u180E\u2002-\u202F\u205F\u2060\u3000"
#
#
# class Expressions2(PartialExpressions):
#     utf_chars: str = r"[:alnum:]\x{00c0}-\x{00d6}\x{00d8}-\x{00f6}\x{00f8}-\x{00ff}"
#     at_signs: str = r"\@\x{ff20}"
#     pound_signs: str = r"\#\x{ff03}"
#     dollar_signs: str = r"\$\x{ff04}"
#     spaces: str = r"\x{0020}\x{00A0}\x{1680}\x{180E}\x{2002}-\x{202F}\x{205F}\x{2060}\x{3000}"
#
#
# class FullExpressions:
#     pass
#
#
# class CryptoCurrency(FullExpressions):
#     # Bitcoin (BTC) wallet address
#     wallet_BTC: str = r"[13][a-km-zA-HJ-NP-Z1-9]{25,34}"
#     # Bitcoin Cash (BCH) wallet address
#     wallet_BCH: str = r"(?:bitcoincash|bchreg|bchtest)\:?(?:q|p)[a-z0-9]{41}"
#     # Ethereum (ETH) wallet address
#     wallet_ETH: str = r"0x[a-fA-F0-9]{40}"
#     # Litecoin (LTC) wallet address
#     wallet_LTC: str = r"[LM3][a-km-zA-HJ-NP-Z1-9]{26,33}"
#     # Dogecoin (DOGE) wallet address
#     wallet_DOGE: str = r"D{1}[5-9A-HJ-NP-U]{1}[1-9A-HJ-NP-Za-km-z]{32}"
#     # Dash (DASH) wallet address
#     wallet_DASH: str = r"X[1-9A-HJ-NP-Za-km-z]{33}"
#     # Monero (XMR) wallet address
#     wallet_XMR: str = r"4[0-9AB][1-9A-HJ-NP-Za-km-z]{93}"
#     # Neo (NEO) wallet address
#     wallet_NEO: str = r"A[0-9a-zA-Z]{33}"
#     # Ripple (XRP) wallet address
#     wallet_XRP: str = r"r[0-9a-zA-Z]{33}"
