from feast import Entity, FeatureView, Field
from feast.types import Float64
from feast.data_source import FileSource
from datetime import timedelta

student = Entity(
    name="student_id",
    join_keys=["student_id"],
)

student_source = FileSource(
    path="../../../../silver/students/data.parquet",
    timestamp_field=None,
)

student_features_view = FeatureView(
    name="student_features",
    entities=[student],
    ttl=timedelta(days=1),
    schema=[
        Field(name="grade", dtype=Float64),
        Field(name="attendance", dtype=Float64),
    ],
    online=False,
    source=student_source,
)