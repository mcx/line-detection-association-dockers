# Copyright (c) 2023, Kirill Ivanov, Anastasiia Kornilova and Dmitrii Iarosh
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from pathlib import Path

from adapter import Adapter
from common.device import Device
from common.parser import create_dl_base_parser, positive_int

if __name__ == "__main__":
    parser = create_dl_base_parser(with_score_directory=False)

    parser.add_argument(
        "--batch",
        "-b",
        metavar="NUM",
        help="dataloader batch size",
        default=1,
        type=positive_int,
    )

    parser.add_argument(
        "--config",
        "-c",
        metavar="PATH",
        dest="base_config",
        help="base model configuration path",
        default=Path(__file__).resolve().parent / "config/eval.yaml",
    )

    parser.add_argument(
        "--model",
        "-M",
        metavar="PATH",
        help="pretrained model path",
        default=Path(__file__).resolve().parent / "weights/deeplsd_wireframe.tar",
    )

    args = parser.parse_args()
    Adapter(
        image_path=Path(args.imgs),
        output_path=Path(args.output),
        lines_output_directory=Path(args.lines_dir),
        scores_output_directory=None,
        config_path=Path(args.base_config),
        pretrained_model_path=Path(args.model),
        device=Device[args.device],
        batch_size=args.batch,
    ).run()
