def build_sales_report(raw: str) -> str:
    """
    `raw` is multi-line text. Each meaningful line has the form
        item , quantity , price
    with arbitrary whitespace around each field.

    Processing rules, applied to every line from splitlines():
      1. Strip the line. Skip it if it is empty or starts
         with "#".
      2. Split on "," . Skip the line if it does not have
         exactly 3 fields.
      3. Strip each field. Skip the line if the quantity field
         is not made only of digits. Convert quantity with
         int() and price with float().
      4. Format the item as title case, truncated to at most 12
         characters (slice AFTER applying title case).
      5. line_total = quantity * price.

    Build these output lines, in order, joined by "\\n" with
    no trailing newline:
      - Header: f"{'ITEM':<12}{'QTY':>4}{'PRICE':>10}{'TOTAL':>12}"
      - One row per valid record, in input order:
          item (width 12, left), quantity (width 4, right),
          price (width 10, right, 2 decimals),
          line_total (width 12, right, 2 decimals, with
          thousands separators)
      - A separator line of 38 "-" characters (use *).
      - Grand total line: "TOTAL" left-aligned in width 26,
        then the sum of all line totals right-aligned in width
        12 with 2 decimals and thousands separators.
      - Summary line:
          f"Rows: {rows} | UTF-8 bytes in items: {bytes_total}"
        where `bytes_total` is the sum of the UTF-8 byte lengths
        of the formatted (title-cased, truncated) item labels.

    If there are no valid records, the report still contains the
    header, separator, a grand total of 0.00, and the summary
    with Rows: 0 and 0 bytes.
    """
    # pass
    rows_data = []
    grand_total = 0.0
    bytes_total = 0
    rows_count = 0

    for line in raw.splitlines():
        stripped = line.strip()
        # Rule 1: Skip empty or comment lines
        if not stripped or stripped.startswith("#"):
            continue
        
        # Rule 2: Split on "," and check field count
        parts = stripped.split(",")
        if len(parts) != 3:
            continue
        
        # Rule 3: Strip each field
        item_raw, qty_raw, price_raw = parts[0].strip(), parts[1].strip(), parts[2].strip()
        
        # Quantity must be made only of digits
        if not qty_raw.isdigit():
            continue
            
        try:
            qty = int(qty_raw)
            price = float(price_raw)
        except ValueError:
            continue
        
        # Rule 4: Format item as title case, truncated to at most 12 chars
        item_formatted = item_raw.title()[:12]
        
        # Rule 5: Calculate line total
        line_total = qty * price
        
        rows_data.append((item_formatted, qty, price, line_total))
        grand_total += line_total
        bytes_total += len(item_formatted.encode("utf-8"))
        rows_count += 1

    # Build output lines
    output_lines = []
    
    # Header
    output_lines.append(f"{'ITEM':<12}{'QTY':>4}{'PRICE':>10}{'TOTAL':>12}")
    
    # Rows
    for item, qty, price, line_total in rows_data:
        output_lines.append(
            f"{item:<12}{qty:>4}{price:>10.2f}{line_total:>12,.2f}"
        )
        
    # Separator line
    output_lines.append("-" * 38)
    
    # Grand total line: "TOTAL" left-aligned in width 26, then grand total in width 12
    output_lines.append(f"{'TOTAL':<26}{grand_total:>12,.2f}")
    
    # Summary line
    output_lines.append(f"Rows: {rows_count} | UTF-8 bytes in items: {bytes_total}")
    
    return "\n".join(output_lines)
