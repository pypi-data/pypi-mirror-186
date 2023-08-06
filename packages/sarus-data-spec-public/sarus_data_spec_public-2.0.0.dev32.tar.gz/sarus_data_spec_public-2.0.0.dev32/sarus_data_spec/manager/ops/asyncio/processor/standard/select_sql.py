import typing as t

import pyarrow as pa

from sarus_data_spec.manager.ops.asyncio.processor.standard.standard_op import (  # noqa: E501
    StandardDatasetOp,
)
import sarus_data_spec.typing as st


class SelectSQL(StandardDatasetOp):
    """Computes schema and arrow
    batches for a dataspec transformed by
    a select_sql transform
    """

    async def schema(self) -> st.Schema:
        # For now not implemented
        raise NotImplementedError

    async def to_arrow(
        self, batch_size: int
    ) -> t.AsyncIterator[pa.RecordBatch]:
        # For now not implemented
        raise NotImplementedError
