import csv
from etl.load import save_to_csv
from etl.transform import transform_posts

def test_save_to_csv_with_sample_data(sample_raw_posts, tmp_path):
    transformed_data = transform_posts(sample_raw_posts["data"])
    output_file = tmp_path / "test_output.csv"
    save_to_csv(transformed_data, output_file)

    assert output_file.exists()

    with output_file.open(newline='', encoding='utf-8-sig') as f:
        reader = list(csv.DictReader(f))

    assert len(reader) == 10
    assert reader[0]["title"] == "Kementerian Ekraf dan CAKAP Latih UMKM Kreatif: Perkuat Talenta, Dorong Transformasi Ekonomi Digital"
    assert reader[0]["user_name"] == "Fachri Wahyudi"
    assert reader[1]["title"] == "Wamen Ekraf Dukung Semangat Kolektif Produk Lokal di The Local Market Edisi Langit Lokal"
    assert reader[1]["user_email"] == "fachriwahyudi@ekraf.go.id"
